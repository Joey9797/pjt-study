[toc]

## 1. Python `json`라이브러리

Python의 `json` 라이브러리는 JSON 형식의 데이터를 Python 객체로 변환하거나, 

Python 객체를 JSON 형식의 문자열로 직렬화(serialize)하는 기능을 제공

주로 웹 API 통신, 파일 입출력, 데이터 저장 등에서 사용



------



## 2. json.loads()

> JSON 형식의 문자열을 Python 객체(주로 dict나 list)로 변환

- **주요 사용 경우** 
  - 외부 소스(예: 파일, 네트워크)로부터 읽어들인 JSON 데이터를 Python에서 쉽게 다루기 위해 사용

### 2.1 사용법 및 옵션

- **기본 사용법:**

  ```python
  import json
  
  json_string = '{"name": "Alice", "age": 30}'
  data = json.loads(json_string)
  
  print(data)  # {'name': 'Alice', 'age': 30}
  print(type(data))  # <class 'dict'>
  ```

- **반환 타입:** JSON 문자열의 구조에 따라 `dict`, `list`, `int`, `float`, `str`, `bool` 등이 반환

- **예외 처리:** 잘못된 JSON 포맷일 경우 `json.JSONDecodeError`가 발생

  ```python
  try:
      data = json.loads(json_string)
  except json.JSONDecodeError as e:
      print("JSON 형식 오류:", e)
  ```



---



## 3. json.dumps()

> Python 객체를 JSON 형식의 문자열로 변환

- **주요 사용 경우** 
  - Python 객체를 외부 시스템에 전송하거나 파일에 저장할 때 JSON 형식으로 변환

### 3.1 사용법 및 옵션

- **기본 사용법:**

  ```python
  import json
  
  data = {"name": "Alice", "age": 30}
  json_string = json.dumps(data)
  
  print(json_string)  # {'name': 'Alice', 'age': 30}
  print(type(json_string))  # <class 'str'>
  ```

- **주요 옵션들:**

  - **`indent`**
     사람이 읽기 좋은 포맷으로 들여쓰기를 적용

    ```python
    json_string = json.dumps(data, indent=4)
    ```

  - **`ensure_ascii`**
     기본값은 `True`로, 비 ASCII 문자를 이스케이프 처리 / `False`로 설정하면 유니코드 그대로 출력

    ```python
    json_string = json.dumps(data, ensure_ascii=False)
    ```

  - **`separators`**
     항목 사이의 구분자(예: `(',', ': ')`)를 지정할 수 있어, 결과 문자열의 공백이나 구분자 스타일을 조절

    ```python
    json_string = json.dumps(data, separators=(',', ': '))
    ```

  - **`sort_keys`**
     결과 문자열에 포함된 키들을 알파벳 순서대로 정렬

    ```python
    json_string = json.dumps(data, sort_keys=True)
    ```

- **반환 타입:** JSON 문자열을 반환하며, 이는 Python의 `str` 타입



------



## 4. 변환 과정 및 예제 코드

JSON 문자열을 Python 객체로 변환한 후(`loads`), 다시 그 객체를 JSON 문자열로 변환(`dumps`)하는 과정

```python
import json

# 원본 JSON 문자열
json_string = '{"name": "Alice", "age": 30}'

# 1. JSON 문자열 -> Python 객체 (loads)
data = json.loads(json_string)
print("loads 결과:", data)
print("loads 결과 타입:", type(data))  # 일반적으로 dict

# 2. Python 객체 -> JSON 문자열 (dumps)
json_result = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)
print("dumps 결과:")
print(json_result)
print("dumps 결과 타입:", type(json_result))  # str
```



---



## 5. 활용 팁

- **데이터 교환:** API 호출 시 받은 JSON 데이터를 `loads`로 파싱하고, 응답 데이터를 `dumps`로 직렬화하여 전송하는 방식으로 활용
- **파일 입출력:** JSON 파일을 읽어 Python 객체로 변환할 때는 `json.load`를, 객체를 파일에 저장할 때는 `json.dump`를 사용
- **디버깅:** `indent` 옵션을 사용하면, 출력 결과를 쉽게 읽고 디버깅할 수 있음
- **국제화:** `ensure_ascii=False`를 사용하면 한글 등 비 ASCII 문자도 올바르게 출력할 수 있음