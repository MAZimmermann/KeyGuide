# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:58:14 2018

@author: MAZimmermann
"""

import requests

with open('credentials.txt', 'r') as f:
    username = str.replace(f.readline(),'\n','')
    clientId = str.replace(f.readline(),'\n','')
    clientSecret = str.replace(f.readline(),'\n','')
    redirect = str.replace(f.readline(),'\n','')
    
    f.close()

def main():
    
    baseURL = 'https://accounts.spotify.com/api/token'
    bodyParams = {'grant_type' : 'client_credentials'}
    
    appReq = requests.post(baseURL, data=bodyParams, auth=(clientId, clientSecret))
    print(appReq)
    print(appReq._content)

main()