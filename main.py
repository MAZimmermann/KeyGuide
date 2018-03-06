# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:58:14 2018

@author: MAZimmermann
"""

import requests
import json

# Grab username, clientId, and clientSecret
with open('credentials.txt', 'r') as f:
    username = str.replace(f.readline(),'\n','')
    clientId = str.replace(f.readline(),'\n','')
    clientSecret = str.replace(f.readline(),'\n','')    
    f.close()

def main():
    
    ########## ########## ########## ########## ##########
    # Request Access Token
    ##########
    
    # Define base url for requesting access token
    tokenRequestURL = 'https://accounts.spotify.com/api/token'
    # Define body parameters for requesting access token
    tokenRequestBody = {'grant_type' : 'client_credentials'}
    
    tokenRequest = requests.post(tokenRequestURL, data=tokenRequestBody, auth=(clientId, clientSecret))
    print('Token Request Status: ',tokenRequest.status_code,'\n')
    
    tokenRequestString = tokenRequest.content
    tokenRequestJSON = json.loads(tokenRequestString)
    
    # Access Token
    token = tokenRequestJSON['access_token']
 
    
    ########## ########## ########## ########## ##########
    # Request Track Information
    ##########

    # Define base url for track request
    apiRequestURL = 'https://api.spotify.com/v1/tracks/3n3Ppam7vgaVa1iaRUc9Lp'
    
    bearerPlusToken = 'Bearer ' + token
    # TODO: Rename this...
    apiRequestHeader = {
    'Authorization': bearerPlusToken
    }

    apiRequest = requests.get(apiRequestURL, headers=apiRequestHeader)
    print('API Request Status: ',apiRequest.status_code,'\n')
    
    apiRequestString = apiRequest.content
    apiRequestJSON = json.loads(apiRequestString)

    print(apiRequestJSON['name'])
    
    # TODO: Define scope?
    # Grab key of song
    # Experiment with audio analysis

main()