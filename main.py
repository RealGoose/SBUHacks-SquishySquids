import http.client
import mimetypes
import json
from hospital import getHospList
# Python Program to Get IP Address
import requests
from requests import get

ip = get('https://api.ipify.org').text
print('Your public IP address is: {}'.format(ip))

#print("Your Computer IP Address is:" + IPAddress)
conn = http.client.HTTPSConnection("api.radar.io")
payload = ''
headers = {
  'Authorization': 'prj_test_sk_9a8f0000f39d8e0eae541935779588195a7d3401',
  'Cookie': '__cfduid=d6dc9a3eeb82f6b63f9ab8bbe607cfa891601077693'
}
conn.request("GET", "/v1/geocode/ip?" + str(ip), payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
json_data = json.loads(data)

print(json_data["address"]["latitude"])
print(json_data["address"]["longitude"])

getHospList(json_data["address"]["latitude"], json_data["address"]["longitude"])
