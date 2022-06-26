import datetime

import requests as r
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080"
# response = r.get(f"{url}/users/me/")
#
# print(response.headers)
# print(response.json())
# print(response.status_code)
#
# response = r.get(f"{url}/users/some_secret_resource/1")
# print(response.headers)
# print(response.json())
# print(response.status_code)


# url = "http://localhost:8080"
# response = r.get(f"{url}/users/me/", auth=HTTPBasicAuth("", ""))
#
# print(response.headers)
# print(response.json())
# print(response.status_code)
#
# response = r.get(f"{url}/users/some_secret_resource/1", auth=HTTPBasicAuth("",""))
# print(response.headers)
# print(response.json())
# print(response.status_code)

#
#
url = "http://localhost:8080"
response = r.get(f"{url}/users/me/", auth=HTTPBasicAuth("SeniorSiarra", "JurekKiler"))

print(response.headers)
print(response.json())
print(response.status_code)

response = r.get(f"{url}/users/some_secret_resource/1", auth=HTTPBasicAuth("SeniorSiarra","JurekKiler"))
print(response.headers)
print(response.json())
print(response.status_code)