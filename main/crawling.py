import requests

URL = "http://www.google.com"
result = requests.get(URL)
print(result.text)
