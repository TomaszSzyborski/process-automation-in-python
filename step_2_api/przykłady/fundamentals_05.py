import datetime

import requests as r

url = "http://localhost:8080"
person = {"first_name": "Ildefons", "last_name": "Gałczyński"}
response = r.post(f"{url}/human/", json=person)

# print(response.json())
# print(response.status_code)
assert response.status_code == 201
url = "http://localhost:8080/get_all_people_sliced?from_number=1000&to_number=1010"
response = r.get(url)
assert response.status_code == 200
assert person in response.json()
print(response.json())
