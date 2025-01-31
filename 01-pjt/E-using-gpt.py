import requests
import json

API_KEY = "0f2f0f78092617a855536b423dfd3af7"

def get_seoul_feels_like():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Seoul,KR&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return round(data["main"]["feels_like"], 1)

CITIES = ["Tokyo,JP", "Beijing,CN", "Bangkok,TH", "Jakarta,ID", "Mumbai,IN", "Manila,PH", "Singapore,SG"]

def find_matching_cities(target_temp):
    matching_cities = []
    print(f"서울의 체감온도: {target_temp}도")  # 서울 체감온도 출력

    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        feels_like = round(data["main"]["feels_like"], 1)

        print(f"{city.split(',')[0]}의 체감온도: {feels_like}도")  # 각 도시의 체감온도 출력

        if feels_like == target_temp:
            matching_cities.append(city.split(",")[0])

    return matching_cities

def main():
    seoul_temp = get_seoul_feels_like()
    same_temp_cities = find_matching_cities(seoul_temp)

    if same_temp_cities:
        print(f"한국의 체감온도는 {seoul_temp}도 입니다. 같은 기온을 가진 도시는 {', '.join(same_temp_cities)} 입니다.")
    else:
        print(f"한국의 체감온도는 {seoul_temp}도 입니다. 같은 기온을 가진 도시는 없습니다.")

if __name__ == "__main__":
    main()
