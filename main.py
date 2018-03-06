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
    
    ##########
    # Request Access Token
    ##########
    
    # Define base url for requesting access token
    baseURL1 = 'https://accounts.spotify.com/api/token'
    # Define body parameters for requesting access token
    bodyParams = {'grant_type' : 'client_credentials'}
    
    appReq = requests.post(baseURL1, data=bodyParams, auth=(clientId, clientSecret))
    
    contentString = appReq.content
    contentJSON = json.loads(contentString)

    # Access Token
    token = contentJSON['access_token']
 
    ##########
    # Request Track Information
    ##########

    # Define base url for track request
    baseURL2 = 'https://accounts.spotify.com/v1//tracks/2TpxZ7JUBn3uw46aR7qd6V'
    
    bearer = 'Bearer' + token
    # TODO: Rename this...
    bearHead = {
    'Authorization': bearer
    }
    
    appReq2 = requests.get(baseURL2, headers=bearHead)
    
    print(appReq2.content)
    
    # TODO: Use access token to access Spotify Web API
    # TODO: Define scope, pull key from song data

main()