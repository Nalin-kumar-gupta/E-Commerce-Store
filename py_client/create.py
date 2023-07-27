import requests

endpoint = 'http://localhost:8000/api/clothes/'

data  = {
    "name": "jacket"
}

response = requests.post(endpoint, json=data)


print(response.json())