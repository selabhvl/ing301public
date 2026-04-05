
# Install the 'requests' module first
# pip3 install requests
import requests

url = "https://dweetr.io/get/latest/dweet/for/ing301"

response = requests.request("GET", url)

print(response.text)
