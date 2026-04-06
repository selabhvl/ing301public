import requests

# Install the 'requests' module first
# pip3 install requests

# https://www.w3schools.com/tags/ref_urlencode.ASP

BASE_URL = "https://dweetr.io/dweet/for/ing301"
PARAMS_STR = "?params=message%3DLecture%20still%20ongoing"

url = BASE_URL + PARAMS_STR

response = requests.request("GET", url)

print(response.text)