import requests
import csv
import json
from requests.api import head

url = 'http://api.openweathermap.org/data/2.5/air_pollution/history?lat=28.7041&lon=77.1025&start=1609502400&end=1640952000&appid=ce0fec27a9435b19b436f5262f9ec86c'

headers = {
    'Accept' : 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
data = json.loads(response.text)
ourdata = []
csvheader = ['DATE','AQI','CO','NO','NO2','O3','SO2','PM_5','PM10','NH3']

for x in data['list']:
    date = x['dt']
    aqi = x['main']['aqi']
    co = x['components']['co']
    no = x['components']['no']
    no2 = x['components']['no2']
    o3 = x['components']['o3']
    so2 = x['components']['so2']
    pm2_5 = x['components']['pm2_5']
    pm10 = x['components']['pm10']
    nh3 = x['components']['nh3']
    listing = [date,aqi,co,no,no2,o3,so2,pm2_5,pm10,nh3]
    ourdata.append(listing)

with open('delhi_aqi.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)

print('done')