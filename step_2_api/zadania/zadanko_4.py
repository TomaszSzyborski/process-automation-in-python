"""
Używając aplikacji Challenge Primer i wiedzy z zadania 3
zautomatyzuj proces zdobywania flag.
Wszystkie flagi zapisz do pliku flags_primer.txt
"""
from pprint import pprint
from faker import Faker

import requests as r

user_name = Faker().name()
flags = []
url = 'http://localhost:8081'
response = r.get(url=f'{url}/challenge/primer/information')
pprint(response.json())

response = r.get(url=f'{url}/challenge/primer/tryout')
pprint(response.json())

response = r.get(url=f'{url}/challenge/primer/flag')
pprint(response.json())

for i in range(10):
    response = r.get(url=f'{url}/challenge/primer/flag/{i}')
    if response.status_code == 200:
        pprint(response.json()['flag'])
        flags.append(response.json()['flag'])

user = {
    'username': user_name,
    'password': 'pass'
}

response = r.post(url=f'{url}/challenge/primer/register', json=user)
response = r.post(url=f'{url}/challenge/primer/register', json=user)
flags.append(response.json()['flag'])

response = r.post(url=f'{url}/challenge/primer/login', json=user)
flags.append(response.cookies.get('session'))

wrong_login = {
    'username': 'fdsafda',
    'password': 'fdssfdf'
}

response = r.post(url=f'{url}/challenge/primer/login', json=wrong_login)
flags.append(response.json()['flag'])
print(flags)


def save_flag(flag):
    flag = flag.replace('$', '')
    flag = flag.replace('{', '')
    flag = flag.replace('}', '')
    flag = flag.replace('"', '')
    return flag


with open('flags_primer.txt', 'w') as f:
    for item in flags:
        f.writelines(f'{save_flag(item)}\n')
