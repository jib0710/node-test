import requests
import json 


 
# city_name:str = input #도시

lang:str = 'kr' #언어
units :str= 'metric' #화씨 온도를 섭씨 온도로 변경



while True:
    city_name = input("도시 : ")
    apiKey:str = "0619d66a168a6ce7b03346faec19924e"
    api:str = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apiKey}&lang={lang}&units={units}" 
    
    response = requests.get(api)
    data = json.loads(response.text)

    
    
    print(f'{city_name}의 날씨: {data["weather"][0]["description"]}')
    print(f'현재 온도:{data["main"]["temp"]}c')
    print(f'체감 온도:{data["main"]["feels_like"]}c')
    
    
    

# JSON 데이터 피싱
# 날씨 정보 출력
# print(f'{city_name}의 날씨: {data["weather"][0]["description"]}')
# print(f'현재 온도:{data["main"]["temp"]}c')
# print(f'체감 온도:{data["main"]["feels_like"]}c')



