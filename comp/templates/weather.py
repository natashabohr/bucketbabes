import requests
import json

endpoint = "http://api.openweathermap.org/data/2.5/weather"
parameters = {"q": "London,UK", "units":"metric", "appid":"4fc7558964b704ba7932d7e122a8766e"}
response = requests.get(endpoint, params = parameters)

data = response.json()
print(data['main'])
print(response.url)
print(response.status_code)
print(response.headers["content-type"])
print(response.text)

print (json.loads(response.text)["main"]["temp"])

for item in json.loads(response.text)["weather"]:
   print(item["main"])

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print ("It's {}C in {}, and the sky is {}".format(temperature, name, weather))

number = raw_input("What temperature is it in London?")
if temperature > 10:
    print "It's warm, you should eat ice cream!"
else:
    print "It's cold, you can go bowling or watch theatre"
print "There's many things to do in London!"
