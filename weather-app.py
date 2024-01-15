import requests, json

api="c358eea1d222e94894d1fdcda3632aad"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city=input("Enter city name: ")
url=base_url+"appid="+api+"&q="+city

response=requests.get(url)

var=response.json()

if(var["cod"])!=404:
    y=var["main"]
    temp=y["temp"]
    temp=(temp)-273.150
    temp_str=str(temp)
    pressure=y["pressure"]
    humidity=y["humidity"]

    z=var["weather"]

    desc=z[0]["description"]

    print(" Temperature (in Celsius) = " +
          temp_str[:6] +
          "\n atmospheric pressure (in hPa unit) = " +
          str(pressure) +
          "\n humidity (in percentage) = " +
          str(humidity) +
          "\n How's Outside? = " +
          str(desc))

else:
    print(" City Not Found ")
