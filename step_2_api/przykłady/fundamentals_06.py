import datetime

import requests as r

url = "http://localhost:8080"
person = {"portfel": "5zł"}
for user_id in range(10):
    response = r.patch(f"{url}/human/{user_id}", json=person)

    print(response.json())
    print(response.status_code)

url = "http://localhost:8080/get_all_people_sliced?from_number=0&to_number=10"
response = r.get(url)
assert response.status_code == 200

print(response.json())
