import requests
import json

url = "https://dweet.io:443/dweet/for/ing301topic"

payload = json.dumps({
  "melding": "forelesning nå i ing301"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
