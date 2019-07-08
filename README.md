# Scrape Business News Headlines
#### Graeme Keleher
#### 20190708

The purpose of this project is to scrape news headlines from nasdaq.com and explore the results with NLP and data visualization. Topics explored include the sentiment distributions of different news sources and the potential cross correlation of daily sentiment and the S&P 500 

## Built With

* Python/Scrapy – Web scraping framework
* Python/TextBlob – Simple sentiment analysis
* R/Tidyverse – Data manipulation and visualization

## Relevant File List 

* daily_scrape.py – wrapper script to execute web scraping and rename resulting csv file with time and date
* headline_sentiment_analysis.py – reads in .csv files output by web scraper, merges them into one data table and performs simple sentiment analysis. Outputs resulting data table as a csv file
* visualize_with_ggplot.R – Takes scraped headlines with sentiment analysis performs and produces visualizations
* scrapy.cfg – Scrapy project config file
* items.py – Scrapy project items file, defines class for scraped objects
* middlewares.py – Scrapy project middlewares file
* pipelines.py – Scrapy project pipelines file, code for writing scraped objects to a csv file
* settings.py – Scrapy project setting file, defines settings for web scraping
* news_spider.py – Scrapy spider for web crawling. Starts with https://www.nasdaq.com/news/, parses article entries for headlines, dates and sources, then continues to the next page with the link on bottom

