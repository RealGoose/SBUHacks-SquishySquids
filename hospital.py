import http.client
import mimetypes
import json

def getHospList(latitude, longitude):
    """
    Returns a list of tuples which represent the latitude and longitude of nearby hopsitals
    """
    conn = http.client.HTTPSConnection("api.radar.io")
    payload = ''
    headers = {
      'Authorization': 'prj_test_pk_6e76504d47441be5e8ad2fc0dcd6daaa57083aa5 '
    }

    latitude = 40.70390
    longitude = -73.98670
    conn.request("GET", "/v1/search/autocomplete?query=hospital&near=" + str(latitude) + "," + str(longitude), payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")


    json_data = json.loads(data)

    #print(json_data)
    addresses = json_data["addresses"]

    long_lat_list = []
    for address in addresses:
        long_lat_list.append((address["latitude"],address["longitude"]))

    print(long_lat_list)
