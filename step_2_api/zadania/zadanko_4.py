"""
Używając aplikacji Challenge Primer i wiedzy z zadania 3
zautomatyzuj proces zdobywania flag.
Wszystkie flagi zapisz do pliku flags_primer.txt
"""
from pprint import pprint

import requests as r

url = "http://localhost:8081/challenge/primer"
response = r.get(f"{url}/information")
pprint(response.json())

response = r.get(f"{url}/tryout")
pprint(response.json())

response = r.get(f"{url}/flag")
pprint(response.json())