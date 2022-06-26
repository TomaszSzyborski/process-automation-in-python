import datetime

import requests as r
from faker import Faker
from requests.auth import HTTPBasicAuth

fake = Faker()
url = "http://localhost:8080"
user = {
  "username": fake.name(),
  "password": "string"
}
response = r.post(f"{url}/register", json=user)

assert response.status_code == 201
print(response.status_code)
print(response.json())

registration_key = response.json()['key']
print(registration_key)

response = r.get(f"{url}/for_logged_in_users_only")
assert response.status_code == 401
assert response.json()['message'] == "I find your lack of cookie disturbing..."

response = r.post(f"{url}/login", json=user)
assert response.status_code == 202
print(response.json())
print(response.cookies)
for cookie in response.cookies:
    print(cookie)

response = r.get(f"{url}/for_logged_in_users_only", cookies=response.cookies)
print(response.status_code)
print(response.json())
print(response.cookies)
print(response.headers)
print(response.cookies[0]['session'])