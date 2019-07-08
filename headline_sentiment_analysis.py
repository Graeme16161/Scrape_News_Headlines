# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:02:34 2019

@author: gakel
"""
###RUN FROM DIRECTORY THAT CONTAINS THE CSV FILES OF SCRAPED DATA

#pandas for data manipulation textblob for simple sentiment analysis
import pandas as pd
from textblob import TextBlob
#import matplotlib.pyplot as plt
import os

#get file names from folder of csv files
files = os.listdir()

#read scraped data into one dataframe and delete duplicate rows
headlines = pd.read_csv(files.pop())

for file in files:
    temp = pd.read_csv(file)
    headlines = pd.concat([headlines,temp])

headlines = headlines.drop_duplicates()

#filter for sources with more than 30 articles
numbers = headlines.groupby('source').size()
top_sources = numbers[numbers>30]
headlines = headlines[headlines['source'].isin(top_sources.index)]

#create sentiment features
headlines['sentiment'] = headlines['headline'].apply(lambda s: TextBlob(s).sentiment)
headlines['polarity'] = headlines['sentiment'].apply(lambda s: s[0])
headlines['subjectivity'] = headlines['sentiment'].apply(lambda s: s[1])
headlines = headlines.drop(columns=['sentiment'])

#Saves processed csv file to current directory
headlines.to_csv("headlines_with_sentiment.csv")


#get mean polarity and subjectivity by headline source
#sentiment_scores = headlines.groupby('source').agg({'polarity': 'mean', 'subjectivity': 'mean'})

#plot mean polarity scores, above 0 is positive, below is negetive
#plt.barh(sentiment_scores.index, sentiment_scores.polarity)
#plt.title("Mean Polarity Scores")
#plt.show()

#plot mean subjectivity scores, the higher the score the more opinon like a headline is
#plt.barh(sentiment_scores.index, sentiment_scores.subjectivity)
#plt.title("Mean Subjectivity Scores")
#plt.show()