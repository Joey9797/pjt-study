import json
import re

def preprocessing():
    # step1 extracted_books.json 파일 읽기
    input_file = "extracted_books.json"
    output_file = "books.json"
    
    with open(input_file, "r", encoding="utf-8") as f:
        books = json.load(f)
    
    # step2 각 도서 항목 순회하며 전처리 진행
    for book in books:
        fields = book.get("fields", {})
        
        # 2-1. description 전처리: &lt; 와 &gt; 같은 HTML 엔티티 제거
        if "description" in fields:
            original_desc = fields["description"]
            # &lt; 와 &gt;를 제거하거나, 필요에 따라 HTML 태그 패턴 제거 (여기서는 단순 제거)
            processed_desc = re.sub(r'&lt;', '', original_desc)
            processed_desc = re.sub(r'&gt;', '', processed_desc)
            fields["description"] = processed_desc
        
        # 2-2. author 전처리: 첫 번째 괄호 '(' 앞까지만 남기기
        if "author" in fields:
            original_author = fields["author"]
            # '(' 이전까지의 텍스트를 추출 (괄호가 없으면 원본 그대로 사용)
            match = re.search(r'^(.*?)\(', original_author)
            if match:
                processed_author = match.group(1).strip()
            else:
                processed_author = original_author
            fields["author"] = processed_author

    # step3 전처리된 결과를 books.json으로 저장
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)
    
    print(f"전처리된 결과가 '{output_file}' 파일에 저장되었습니다.")

if __name__ == '__main__':
    preprocessing()
