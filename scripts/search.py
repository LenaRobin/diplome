#!/usr/bin/env python2.7
# -*- coding: iso-8859-1 -*-
#on veut utiliser la bibliothèque tweepy pour utiliser l'API twitter
import tweepy
from bs4 import BeautifulSoup
import re
import urllib2
import sys
#paramètres pour avoir accès au compte
consumer_key = 'LM8VAfbv6Nj9A75RIAi9Bym23' 
consumer_secret = 'eqAH40Lm8RZOaClQ0O22b6c8cPb8b4In0pZN1wxq4SQwSil0OX' 
access_token = '2977712217-CBVlSgRSwocakWfjmtr7GJICArYkkiVtrXVNQMd'
access_token_secret = 'IpnilDp9mkgqMhQimEBXhRMaK54Sk64ze8kHma8Y2CwDg'

#authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
   
#connexion sur l'API
api = tweepy.API(auth)  

#récupération de tag
soup = BeautifulSoup(?)
for tag in soup.find_all('div', attrs={'class': 'tags'}):
    tags = tag.text.replace(',','').replace('[','').replace(']','')




#recherche de contenu
for tweet in tweepy.Cursor(api.search,
                            q=tags +"(-hoax)(-rumor)(-fake)",  #terme de la recherche
                            include_entities=True,
                            count=30, 
                            show_users=True).items():      
#    contenu = tweet.text + tweet.user.screen_name + str(tweet.created_at)
    contenu = "<div class=\"twitter_bloc\">" + "<div class=\"twitter_user\">" + tweet.user.screen_name + "</div>" + "<div class=\"twitter_text\">" + tweet.text + "</div>" + "<div class=\"twitter_date\">" + str(tweet.created_at) + "</div>" + "</div>"
    #afficher le contenu des tweets
    print contenu.encode('ascii','ignore')
    #enregistrer le contenu dans un fichier

