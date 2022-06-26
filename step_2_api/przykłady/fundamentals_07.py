import datetime

import requests as r

url = "http://localhost:8080"
# response = r.get(f"{url}/header_check/")
#
# print("Before setting headers")
# print(response.headers)
# print(response.json())
# print(response.status_code)

headers = {"apikey": "woohoo", 'content-type': 'application/json'}
response = r.get(f"{url}/header_check/", headers=headers)
print("After setting headers")
print(response.headers)
print(response.json())
print(response.status_code)
print(response.cookies)
