#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

endpoint = 'http://127.0.0.1:5000/'

def get():
    url = endpoint + 'test/get'
    response = requests.get(url)
    print(response.url)
    print(response.text)

def get2():
    url = endpoint + 'test/get/1'
    response = requests.get(url)
    print(response.url)
    print(response.text)

def post():
    url = endpoint + 'test/post'
    payload = {'desc': 'test'}
    headers = {'content-type': 'application/json'}
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers)
    print(response.url)
    print(response.text)

get()
get2()
post()
