# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:58:14 2018

@author: MAZimmermann
"""

import spotipy
import spotipy.util as util

#parameters for client information on Spotify's API
scope = 'user-library-read'

with open('credentials.txt', 'r') as f:
    username = str.replace(f.readline(),'\n','')
    clientId = str.replace(f.readline(),'\n','')
    clientSecret = str.replace(f.readline(),'\n','')
    redirect = str.replace(f.readline(),'\n','')
    
    f.close()

#attempts access to Spotify's API - post redirected URL in the console
token = util.prompt_for_user_token(username, scope,
                                   client_id=clientId, 
                                   client_secret=clientSecret,
                                   redirect_uri = redirect)

def main():