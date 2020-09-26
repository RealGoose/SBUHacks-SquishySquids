import http.client
import mimetypes
import json
from distanceRequest import getDistance
def getHospList(latitude, longitude):
    """
    Prints a list of formatted addresses of nearby hopsitals
    """
    conn = http.client.HTTPSConnection("api.radar.io")
    payload = ''
    headers = {
      'Authorization': 'prj_test_pk_6e76504d47441be5e8ad2fc0dcd6daaa57083aa5 '
    }


    conn.request("GET", "/v1/search/autocomplete?query=hospital&near=" + str(latitude) + "," + str(longitude) + "&limit=5", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")


    json_data = json.loads(data)

    #print(json_data)
    addresses = json_data["addresses"]

    d_list = []

    formatted_address_list = []
    for address in addresses:
        formatted_address_list.append(address["formattedAddress"])
        #d_list.append((address["latitude"],address["longitude"]))
        getDistance(latitude, longitude, address["latitude"], address["longitude"])

    print(d_list)
    print(formatted_address_list)
