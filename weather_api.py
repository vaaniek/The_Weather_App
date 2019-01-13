import http.client
import json
import weather_callings

def get_city_name():
    global cityname
    cityname = input("What city would you like to see the weather for? ")
    return cityname

def current_or_5_day_forecast():
    global choice
    while True:
        try:
            choice=input("Would you like the current forecast or a 5 day forcast? Enter as current or 5 day. ")
        except NameError:
            print("Enter either current or 5 day")
        if((choice=="current")or(choice=="5 day")):
            break
        else:
            print("Enter either current or 5 day")
            continue
    return choice    

get_city_name()
'''
current_or_5_day_forecast()
if(choice=="current"):
    weather_callings.current_weather_data(cityname)
else:
    weather_callings.five_day_weather_data(cityname)
'''
weather_callings.five_day_weather_data(cityname)
