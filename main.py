import http.client
import mimetypes
import requests
from requests import get

#Users ip address
ip = get('https://api.ipify.org').text
print('Your public IP address is: {}\n'.format(ip))

#Latitude and Longtitude of the User's IP address
url = "http://ip-api.com/json/"+ ip + "?fields=lat,lon"
payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
printable_response = str(response).strip("\'b")
print(response.text.encode('utf8'))
print('\n')


#Actual Radar query
conn = http.client.HTTPSConnection("api.radar.io")
payload = ''
headers = {
  'Authorization': 'prj_test_sk_9a8f0000f39d8e0eae541935779588195a7d3401',
  'Cookie': '__cfduid=d6dc9a3eeb82f6b63f9ab8bbe607cfa891601077693'
}
conn.request("GET", "/v1/geocode/ip?" + str(ip), payload, headers)
res = conn.getresponse()
data = res.read()
#Messy Radar Output:
#print(data.decode("utf-8"))
