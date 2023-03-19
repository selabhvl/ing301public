import requests

url = "https://dweet.io:443/get/latest/dweet/for/ing301"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)