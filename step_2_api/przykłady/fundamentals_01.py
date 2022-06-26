import datetime

import requests as r

url = "http://localhost:8080/ok"
response = r.get(url)
assert response.status_code == 200
print(response)
"""
{
  "basicInformation": "This is GET example for status code 200",
  "responseInformation": {
    "shortDescription": "OK",
    "longDescription": "The request has succeeded"
  },
  "timestamp": "2022-06-24 11:25:09.604893"
}
"""

body = response.json() # to jest dict
print(response.text)
print(type(response.text))
print(body)
print(type(body))

print(body['basicInformation'])
print(type(body['responseInformation']))
print(body['responseInformation']['longDescription'])
print(body['timestamp'])
print(type(body['timestamp']))

# print(body['timestamp'] < datetime.datetime.now())
print(datetime.datetime.strptime(body['timestamp'], "%Y-%m-%d %H:%M:%S.%f") < datetime.datetime.now())
#
delta = datetime.timedelta(seconds=-1)
print(datetime.datetime.strptime(body['timestamp'], "%Y-%m-%d %H:%M:%S.%f") > datetime.datetime.now() + delta)


#  url = 'http://example.com/some/cookie/setting/url'
#  r = requests.get(url)
#  r.cookies
# {'example_cookie_name': 'example_cookie_value'}
#
# give cookie back to server on subsequent request
#
#  url = 'http://httpbin.org/cookies'
#  cookies = {'cookies_are': 'working'}
#  r = requests.get(url, cookies=cookies)`