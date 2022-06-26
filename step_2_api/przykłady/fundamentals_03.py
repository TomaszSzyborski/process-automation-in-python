import requests as r

# f_name = "Ada"
# l_name = "Droś"

users = [
    {
        "f_name": "Ada",
        "l_name": "Droś"
    }
]

for user in users:
    url = f"http://localhost:8080/query_params?first_name={user['f_name']}&last_name={user['l_name']}"
    response = r.get(url)
    assert response.status_code == 200

    print(response.json())
