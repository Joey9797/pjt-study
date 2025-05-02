import json

def create_fixture(raw_json_file, category_json_file, extracted_json_file):
    # step 1 파일 읽기: books_raw.json과 category.json에서 데이터 로드
    with open(raw_json_file, "r", encoding="utf-8") as f:
        books = json.load(f)
    with open(category_json_file, "r", encoding="utf-8") as f:
        categories = json.load(f)
    
    # step 2 각 카테고리별 추출된 도서 수를 추적 (category.json의 pk를 사용)
    category_counts = {category["pk"]: 0 for category in categories}
    
    extracted_books = []
    fixture_pk = 1

    # step 3 book_raw.json의 각 도서의 categoryId 순차 조회
    # 3-1. categories.json의 각 카테고리에서 cid 리스트에 해당 categoryId가 존재하는지 확인
    for book in books:
        item = book.get("item", {})
        fields = item[0]            
        orig_cat = fields.get("categoryId")
        orig_cat_int = int(orig_cat)
        
        for category in categories:
            cid_list = category.get("cid", [])
            if orig_cat_int in cid_list:
                # 3-2. 해당 카테고리에서 현재까지 추출된 도서 수 확인
                cat_pk = category.get("pk")
                if category_counts.get(cat_pk, 0) < 10:
                    # 3-3. 10권 이하라면, 도서의 categoryId를 해당 카테고리의 pk(cat_pk)로 매핑 후 extracted_books에 저장
                    fixture_fields = {"category": cat_pk}
                    keys_to_copy = [
                        "title",
                        "description",
                        "isbn13",
                        "cover",
                        "publisher",
                        "pubDate",
                        "author",
                        "customerReviewRank",
                    ]
                    for key in keys_to_copy:
                        if key in fields:
                            if key == "customerReviewRank":
                                fixture_fields["customer_review_rank"] = fields[key]
                            elif key == "pubDate":
                                fixture_fields["pub_date"] = fields[key]
                            elif key == "isbn13":
                                fixture_fields["isbn"] = fields[key]
                            else:
                                fixture_fields[key] = fields[key]
                    
                    fixture_entry = {
                        "model": "books.book",
                        "pk": fixture_pk,
                        "fields": fixture_fields
                    }
                    
                    extracted_books.append(fixture_entry)
                    fixture_pk += 1
                    category_counts[cat_pk] += 1
                break  # 해당 도서가 하나의 카테고리에 매칭되거나 이미 10권이 넘었다면 끝
    
    # step4 결과를 JSON 파일로 저장
    with open(extracted_json_file, "w", encoding="utf-8") as f:
        json.dump(extracted_books, f, ensure_ascii=False, indent=4)
    
    print(f"총 {len(extracted_books)}개의 fixture 항목이 '{extracted_json_file}'에 저장되었습니다.")

if __name__ == "__main__":
    raw_json_file = "01_books_raw.json"
    category_json_file = "categories.json"
    extracted_json_file = "extracted_books.json"
    create_fixture(raw_json_file, category_json_file, extracted_json_file)
