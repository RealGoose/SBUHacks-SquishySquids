import http.client
import mimetypes
# Python Program to Get IP Address
import socket
hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)

print("Your Computer IP Address is:" + IPAddress)
conn = http.client.HTTPSConnection("api.radar.io")
payload = ''
headers = {
  'Authorization': 'prj_test_sk_9a8f0000f39d8e0eae541935779588195a7d3401',
  'Cookie': '__cfduid=d6dc9a3eeb82f6b63f9ab8bbe607cfa891601077693'
}
conn.request("GET", "/v1/geocode/ip?" + str(IPAddress), payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
