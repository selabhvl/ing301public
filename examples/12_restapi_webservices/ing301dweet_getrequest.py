# Install the 'requests' module first
# pip3 install requests

import requests

url = "https://dweet.io:443/get/latest/dweet/for/ing301topic"

payload= {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
