import json
import pandas as pd


def cid_grouping(excel_file, json_file) :
    # step 1 엑셀 파일 읽기: 첫 2행은 건너뛰고 3번째 행(0-index 기준 2번 행)을 헤더로 사용
    df = pd.read_excel(excel_file, header=2)

    # step 2 "1Depth" 값을 기준으로 CID 그룹핑
        # step 2-1
    category_dict = {}
    for index, row in df.iterrows():
        category = row['1Depth']
        cid = row['CID']
        # 카테고리 값이 NaN인 경우는 무시
        if pd.isna(category):
            continue
        
        # 카테고리별로 CID를 리스트에 추가
        # category_dict[category] = category_dict.get(category, []).append(cid)
        if category in category_dict:
            category_dict[category].append(cid)
        else:
            category_dict[category] = [cid]
    print('step2-1 결과 :', len(category_dict), category_dict)


    # step 2-2 각 그룹에 pk 부여, cid_list를 함께 저장
    new_groups = []
    for idx, (cat, cid_list) in enumerate(category_dict.items(), start=1):
        new_groups.append({
            'pk': idx,
            'name': cat,
            'cid_list': cid_list
        })
    print('step2-2 결과 :', len(new_groups), new_groups)


    # step 3 7개 그룹으로 병합
    new_group_mapping = {
        1: {"name": "소설/시/희곡", "old_pks": [12]},
        2: {"name": "경제/경영", "old_pks": [3]},
        3: {"name": "자기계발", "old_pks": [9, 19, 23]},
        4: {"name": "인문/교양", "old_pks": [5, 11, 15, 17, 18, 21, 27, 28]},
        5: {"name": "취미/실용", "old_pks": [1, 2, 10, 16]},
        6: {"name": "어린이/청소년", "old_pks": [14, 20, 30, 31]},
        7: {"name": "과학", "old_pks": [6, 33]},
    }
    

    final_groups = []
    for new_pk, mapping_data in new_group_mapping.items():
        merged_cid_list = []
        for old_pk in mapping_data["old_pks"]:
            # new_groups 리스트에서 pk가 old_pk와 일치하는 항목을 찾음
            for group in new_groups:
                if group["pk"] == old_pk:
                    merged_cid_list.extend(group["cid_list"])
                    break
        final_groups.append({
            "pk": new_pk,
            "name": mapping_data["name"],
            "cid": merged_cid_list
        })
    print('step3 결과 :', len(final_groups), final_groups)


    # step4 최종 JSON 파일로 저장
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(final_groups, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    excel_file = '02_aladin_Category_CID_20210927.xls'     # 엑셀 파일 경로
    json_file = 'categories.json'                         # 생성할 JSON 파일 경로
    cid_grouping(excel_file, json_file)
    print(f"JSON 파일 '{json_file}'이(가) 생성되었습니다.")
