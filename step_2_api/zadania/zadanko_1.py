"""
Używając aplikacji Fundamentals i sekcji "Successful requests responses"
zmodyfikuj listę ludzi używając poszczególnych endpointów.
Za każdym razem sprawdź poprawność modyfikacji.
"""
import requests as r

url = "http://localhost:8080"
response = r.get(url=f'{url}/get_all_people')

body = response.json()
print(len(body.keys()))

response = r.get(url=f'{url}/human/33')
human = response.json().get('human')
assert human['last_name'] == 'Piguła'

last_name = {"last_name": "Kowalski"}
response = r.patch(url=f'{url}/human/34', json=last_name)
print(response.status_code)

response_check = r.get(url=f'{url}/human/34')
print(response_check.json())

name = {
    'first_name': 'Adam',
    'last_name': 'Kowalski'
}
response = r.put(url=f'{url}/human/35', json=name)
assert response.status_code == 202

response = r.get(url=f'{url}/human/35')
print(response.json()['human'])


name = {
    'first_name': 'Jan',
    'last_name': 'Kowalski'
}
response = r.post(url=f'{url}/human', json=name)
assert response.status_code == 201





