import requests

url: str = " http://numbersapi.com/43"
response = requests.get(url)

print(response.text if response.status_code == 200 else response.status_code)