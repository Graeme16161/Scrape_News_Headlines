# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:02:34 2019

@author: gakel
"""
#pandas for data manipulation textblob for simple sentiment analysis
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


#read scraped data
headlines = pd.read_csv("nasdaw_headlines_data.csv")


#create sentiment features
headlines['sentiment'] = headlines['headline'].apply(lambda s: TextBlob(s).sentiment)
headlines['polarity'] = headlines['sentiment'].apply(lambda s: s[0])
headlines['subjectivity'] = headlines['sentiment'].apply(lambda s: s[1])

#get sources with more than 10 articles
numbers = headlines.groupby('source').size()
top_sources = numbers[numbers>10]

#get mean polarity and subjectivity by headline source

headlines = headlines[headlines['source'].isin(top_sources.index)]
sentiment_scores = headlines.groupby('source').agg({'polarity': 'mean', 'subjectivity': 'mean'})



#plot mean polarity scores, above 0 is positive, below is negetive
plt.barh(sentiment_scores.index, sentiment_scores.polarity)
plt.title("Mean Polarity Scores")
plt.show()


#plot mean subjectivity scores, the higher the score the more opinon like a headline is
plt.barh(sentiment_scores.index, sentiment_scores.subjectivity)
plt.title("Mean Subjectivity Scores")
plt.show()