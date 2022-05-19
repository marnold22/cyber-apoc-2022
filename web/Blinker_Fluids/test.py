#!/usr/bin/env python3
import requests

url = 'http://46.101.6.238:31172/'
data = {}

response = requests.post(url, json=data)
print("Status Code", response.status_code)
print("JSON Response ", response.json())