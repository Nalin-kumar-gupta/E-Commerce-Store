import requests

endpoint = 'http://localhost:8000/api/clothes/2/'
response = requests.get(endpoint)


print(response.json())