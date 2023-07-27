import requests

endpoint = 'http://localhost:8000/api/clothes/1/update/'

data = {
    "name": "cool",
    "price": 67.28,
    "description": "tis is too good"
}

response = requests.put(endpoint, json=data)


print(response.json())