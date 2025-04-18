import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_google_data(keyword):
    """
    지정된 키워드를 사용하여 Google 검색 결과 페이지의 HTML을 가져온 뒤,
    BeautifulSoup을 통해 구조화된 결과물에서 제목들을 추출하고, 해당 결과를 txt 파일에 저장합니다.

    :param keyword: 구글에 검색하고 싶은 키워드(문자열)
    """
    # 1) 검색 URL 생성
    url = f"https://www.google.com/search?q={keyword}"

    # 2) 크롬 옵션 객체 생성
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    )
    # 자동화 탐지 우회 옵션 추가
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("disable-blink-features=AutomationControlled")

    # 3) Service 객체를 통해 크롬 드라이버 실행
    service = Service(
        ChromeDriverManager().install()  # ChromeDriverManager를 사용하여 드라이버 자동 설치
    )
    driver = webdriver.Chrome(service=service, options=options)

    # 4) 구글 검색 결과 페이지로 이동
    driver.get(url)

    # 페이지 로딩 대기
    time.sleep(5)

    # 5) 페이지의 HTML 소스 가져오기
    html = driver.page_source

    # 6) BeautifulSoup 객체 생성(파서: html.parser)
    soup = BeautifulSoup(html, "html.parser")

    # 7) 검색 결과에서 제목 추출
    results = soup.select("div.notranslate")
    titles = []  # 결과 제목을 저장할 리스트
    for result in results:
        title = result.select_one(".VuuXrf")
        if title is not None:
            title_text = title.get_text().strip()
            print("제목 =", title_text)
            titles.append(title_text)

    # 8) 추출한 결과 제목들을 별도의 txt 파일에 저장
    with open("04_result.txt", "w", encoding="utf-8") as result_file:
        for idx, title in enumerate(titles, 1):
            result_file.write(f"{idx}. {title}\n")

    # 9) 작업 완료 후 웹드라이버 종료
    driver.quit()


# 검색어 설정 및 함수 실행
keyword = "파이썬"
get_google_data(keyword)
