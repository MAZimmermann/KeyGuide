# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:58:14 2018

@author: MAZimmermann
"""

import requests

# Grab username, clientId, and clientSecret
with open('credentials.txt', 'r') as f:
    username = str.replace(f.readline(),'\n','')
    clientId = str.replace(f.readline(),'\n','')
    clientSecret = str.replace(f.readline(),'\n','')    
    f.close()

def main():
    
    # define base url
    baseURL = 'https://accounts.spotify.com/api/token'
    
    # define body parameters
    bodyParams = {'grant_type' : 'client_credentials'}
    
    appReq = requests.post(baseURL, data=bodyParams, auth=(clientId, clientSecret))
    print(appReq)
    print(appReq._content)

    # TODO: Define scope, pull key from song data

main()