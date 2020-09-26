import http.client
import mimetypes
import json
conn = http.client.HTTPSConnection("api.radar.io")
payload = ''
headers = {
  'Authorization': 'prj_test_pk_6e76504d47441be5e8ad2fc0dcd6daaa57083aa5 '
}
conn.request("GET", "/v1/search/autocomplete?query=brooklyn+roasting&near=40.70390,-73.98670", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")


json_data = json.loads(data)

#print(json_data)
addresses = json_data["addresses"]

long_lat_list = []
for address in addresses:
    long_lat_list.append((address["latitude"],address["longitude"]))

print(long_lat_list)
