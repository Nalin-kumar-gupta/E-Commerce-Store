import requests

endpoint = 'http://localhost:8000/api/'
response = requests.post(endpoint, json={"name": "Abc1237678", "description": "jhbjhhjbhjh", "price": 988})

print(response.text)
print(response.status_code)