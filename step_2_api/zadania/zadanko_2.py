"""
Używając aplikacji Fundamentals i sekcji "Client error requests responses"
napisz odpowiednie requesty i sprawdź responsy przy użyciu python requests
"""
import requests as r
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080"
user = {
    'Username': 'Captain_snack',
    'password': 'LateNightSausage'}

response = r.get(url=f'{url}/limited', auth=HTTPBasicAuth('',''))
assert response.status_code == 401

response = r.get(url=f'{url}/limited', auth=HTTPBasicAuth('Captain_snack', 'LateNightSausage'))
assert response.status_code == 200
