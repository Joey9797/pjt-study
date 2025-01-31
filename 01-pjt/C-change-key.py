import copy
import json
import requests
import pprint

def get_deposit_products():
    
    API_KEY = "0f2f0f78092617a855536b423dfd3af7"
    lat = 37.56
    lon = 126.97 
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    
    result = requests.get(URL).json()
    return result

data = get_deposit_products()


def getDataValue(*args):
    dataValue = {}
    for arg in args:
        value = data[arg]
        if isinstance(value, list):
            dataValue[arg] = value[0]
        else :
            dataValue[arg] = value

    return dataValue


# pprint.pprint(getDataValue('main', 'weather'))

def getNewData(krData):
    engData = getDataValue('main', 'weather')
    dataKey1 = list(engData.keys())
    newDict = {}
    for key1 in engData:
        for key2 in engData[key1]:
            if key2 
    # for krKey in krData:
    #     if krKey in dataKey1:
    #         newDict[krData[krKey]] = engData[krKey]
    #         for list(engData[krKey].keys())
    # return list(engData[krKey].keys())



krData = {'feels_like' : '체감온도',
          'humidity' : '습도',
          'pressure' : '기압',
          'temp' : '온도',
          'temp_max' : '최고온도',
          'temp_min' : '최저온도',
          'description' : '요약',
          'icon' : '아이콘',
          'main' : '핵심' ,
          'id' : '식별자',
          'weather' : '날씨',
          }

pprint.pprint(getNewData(krData))



    
# pprint.pprint(getDataValue('main', 'weather'))