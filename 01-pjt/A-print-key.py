def get_deposit_products():
    
    API_KEY = "0f2f0f78092617a855536b423dfd3af7"
    lat = 37.56
    lon = 126.97 
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    
    result = requests.get(URL).json()
    return result



data = get_deposit_products()
pprint.pprint(data)