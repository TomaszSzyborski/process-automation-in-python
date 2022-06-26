import datetime

import requests as r

url = "http://localhost:8080/get_all_people_sliced?from_number=1&to_number=10"
response = r.get(url)
assert response.status_code == 200

# print(response.json())

body = response.json()

print(isinstance(body, list))

# for user in body:
#     print(user)