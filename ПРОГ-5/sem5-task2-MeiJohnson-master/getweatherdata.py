import requests
import json

def get_weather_data(place:str, api_key: str = None):
    # напишите здесь ваш код
    
    result = None

    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={api_key}')
        temp = json.loads(response.text)
        timez = temp['timezone']//3600
        if (timez >= 0): 
            timez = '+' + str(timez)
        else:
            str(timez)
        information = {'name':temp['name'],'coord':{'lon':temp['coord']['lon'],'lat':temp['coord']['lat']}, 'country':temp['sys']['country'], 
        'feels_like': temp['main']['feels_like'], 'timezone':f"UTC{timez}"}
        result = json.dumps(information)
    except Exception as e:
        print("Exception:", e)
   
    return result

if __name__ == "__main__":
    with open("api.txt") as file_handler:
        apiId = file_handler.read()
        get_weather_data('Чикаго,US', apiId)

    try:
        assert ("Chicago" in get_weather_data('Чикаго,US', apiId))
    except:
        print('Тест провален, результат неверный')

    try:
        assert ("Saint Petersburg" in get_weather_data('Санкт-Петербург,RU', apiId))
    except:
        print('Тест провален, результат неверный')
    
    try:
        assert ("Dhaka" in get_weather_data('Дакка,BD', apiId))
    except:
        print('Тест провален, результат неверный')
    
    try:
        assert type(get_weather_data('Дакка,BD', apiId)) == str
    except:
        print('Тест провален, результат неверный')

  
