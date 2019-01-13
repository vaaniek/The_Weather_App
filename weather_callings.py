import http.client
import json

#api key: 200fc5f09a8b7dbdcaba9696e065a971

class Weather():
    def __init__(self,datetime,temp):
        self.datetime=datetime
        self.temp=temp

def current_weather_data(cityname):
    conn=http.client.HTTPSConnection("api.openweathermap.org")
    conn.request("GET","/data/2.5/weather?q="+cityname+"&appid=200fc5f09a8b7dbdcaba9696e065a971")
    res = conn.getresponse()
    data=res.read()
    jsonResults=json.loads(data.decode("utf-8"))
    tempKelvin=jsonResults["main"]["temp"]
    temperature=str(int(tempKelvin)-273)
    description=jsonResults["weather"][0]["description"]
    print("Right now, there is "+description+" with a temperature of "+temperature+"°C")

def five_day_weather_data(cityname):
    conn=http.client.HTTPSConnection("api.openweathermap.org")
    conn.request("GET","/data/2.5/forecast?q="+cityname+"&appid=200fc5f09a8b7dbdcaba9696e065a971")
    res = conn.getresponse()
    data=res.read()
    jsonResults=json.loads(data.decode("utf-8"))
    for i in jsonResults["list"]:
        datetime=i["dt_txt"]
        temp=str(int(i["main"]["temp"])-273)
        weather=Weather(datetime,temp)
        print("The weather for this date and time is "+weather.datetime+" and the temperature is "+weather.temp)
      
    

