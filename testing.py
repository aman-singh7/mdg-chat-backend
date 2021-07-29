import requests

url = 'http://127.0.0.1:8000/'

# 1: Send GET request to /new/ with 'name',
response1 = requests.get(url + 'new/', params={'name': 'user'})

# 2: You'll get back username and password in a json,
# 3: Send POST request to /token/ with that json,
response2 = requests.post(url + 'token/', data=response1.json())

# 4: You'll get back a token,
token = response2.json()['token']

# 5: Send GET request to /demo/ with 'token'
headers = {
    'Authorization': f'Token {token}',
}
response3 = requests.get(url + 'demo/', headers=headers)
print(response3)
print(response3.json())
