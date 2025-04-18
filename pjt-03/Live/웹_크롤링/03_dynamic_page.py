import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_google_data(keyword):
    """
    지정된 키워드를 사용하여 Google 검색 결과 페이지를 로드한 후,
    페이지의 HTML 소스를 추출하여 BeautifulSoup으로 파싱하고,
    검색 결과의 제목 정보를 출력합니다.

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
    # 자동화 탐지 우회 옵션
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

    # 7) div 태그 중 class 가 VuuXrf 인 요소(검색 결과의 제목) 검색 및 출력
    result_stats = soup.select_one(".VuuXrf")
    print(result_stats.text)

    # 8) 작업 완료 후 웹드라이버 종료
    driver.quit()


# 검색어 설정
keyword = "파이썬"
get_google_data(keyword)
