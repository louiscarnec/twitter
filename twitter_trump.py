#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:25:10 2017

@author: Carnec
"""

""" Inspired by http://adilmoujahid.com/posts/2014/07/twitter-analytics/"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

tweets_data_path = '/Users/Carnec/Documents/DataScience/twitter/twitter_data_trump.json'


tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
 
tweets = pd.DataFrame()    
tweets['text'] = list(map(lambda tweet: tweet.get('text'), tweets_data)) # python.3 need 
#to use list with map and use .get() to get text from list
tweets['lang'] = list(map(lambda tweet: tweet.get('lang'), tweets_data))
tweets['country'] = list(map(lambda tweet: tweet.get('place').get('country') if tweet.get('place') != None else None, tweets_data))


""" Seaborn """
languagecount = tweets['lang'].value_counts()
languagecount = pd.DataFrame({'language':languagecount.index, 'values':languagecount.values})

sns.barplot(x = 'language', y = 'values', data=languagecount)    

""" mining text """
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets = tweets.dropna(axis=0, how='all') #drop None/NA   
    
tweets['bike1'] = tweets.get('text').apply(lambda tweet: word_in_text('bike', tweet))
tweets['bike2'] = tweets.get('text').apply(lambda tweet: word_in_text('cycling', tweet))

tweets.text[tweets['bike1']==True]
tweets.text[tweets['bike2']==True]
    
""" trump adviser george papadopoulos and the lies about russian links """
tweets['adviser'] = tweets.get('text').apply(lambda tweet: word_in_text('papadopoulos', tweet))
tweets['adviser'].value_counts()
tweets.text[tweets['adviser']==True]

    
    
    