#!/usr/bin/env python3
import requests

url = 'http://165.22.123.39:32629/login'
data = {
    "username": "marnold",
    "password": "password",
    }

response = requests.post(url, json=data)
print("Status Code", response.status_code)
print("JSON Response ", response.json())