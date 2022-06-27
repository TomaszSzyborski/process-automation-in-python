"""
Używając aplikacji Reactor Challenge i wiedzy z zadania 3 i 4
zautomatyzuj proces zdobywania flag.
Wszystkie flagi zapisz do pliku flags_reactor.txt
"""
from pprint import pprint
from faker import Faker
import requests as r

url = 'http://localhost:8080'

flags = []

# odbieramy klucz
respond = r.post(url=f'{url}/challenge/reactor/desk', json={
    'name': Faker().name()
})

key = respond.json()['key']
print(key)

# control room z blednym kluczem
respond = r.get(url=f'{url}/challenge/reactor/gafdgfdds/control_room')
flags.append(respond.json()['message'][-18:])

# sprawdzenie reaktora z dobrym kluczem
respond = r.get(url=f'{url}/challenge/reactor/{key}/reactor_core')
flags.append(respond.json()['flag'])

# AZ-5 button
respond = r.put(url=f'{url}/challenge/reactor/{key}/control_room/az_5', json={
    'pressed': 'true'
})
flags.append(respond.json()['flag'])

# reset reaktora z dobrym kluczem
respond = r.get(url=f'{url}/challenge/reactor/{key}/reset_progress')
flags.append(respond.json()['flag'])

# reset reaktora z błędnym kluczem
respond = r.get(url=f'{url}/challenge/reactor/gdfgag/reset_progress')
flags.append(respond.json()['flag'])

# remove fuel rods
for i in range(0, 50):
    respond = r.delete(url=f'{url}/challenge/reactor/{key}/control_room/fuel_rods/{i}')
    pprint(respond.json())


# remove contorl rods
for i in range(0, 20):
    respond = r.delete(url=f'{url}/challenge/reactor/{key}/control_room/control_rods/{i}')
    pprint(respond.json())

# analysis
respond = r.get(url=f'{url}/challenge/reactor/{key}/control_room/analysis')
pprint(respond.json())
print(respond.cookies)

print(flags)


