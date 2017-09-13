#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import BeautifulSoup
import json
from urllib2 import urlopen

with open('config.json', 'r') as f:
    config = json.load(f)
    
#variables à utiliser
url=config["url"]["connexion"]
identifier=config["credentials"]["id"]
password=config["credentials"]["pass"]

#récupération du token
def get_token(raw_resp):
    soup = BeautifulSoup.BeautifulSoup(raw_resp.text)
    token = soup.find('input',attrs={'type':'hidden','value':'1'})['name']
    return token


#création d'un payload avec les data contenues dans le fichier de config
payload = {
    'username': identifier,
    'password': password,
    }

#envoi des data
with requests.session() as s:
    resp = s.get(url)
    payload['token'] = get_token(resp)
    response_post = s.post(url, data=payload)
    print(response_post)
