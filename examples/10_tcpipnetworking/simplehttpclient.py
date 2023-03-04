# NOTE: request module must be installed using:
# python3 -m pip install requests

import requests

# Let the user provide the URL of the resource to be retreived
url = input("URL:>")

# Send the HTTTP GET Request
response = requests.get(url)

# Print the body of the HTTP response being returned
print(response.text)

response.close()

