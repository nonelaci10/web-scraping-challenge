from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd 
import time
import pymongo
import requests

#Executable path
def init_browser():
    executable_path = {"executable_path": chromedriver.exe}
    return Browser('chrome'. **executable_path, headless=False)


#Mars work and data
def mars_news(browser):
    url = "https://mars.nasa.gov/news/8415/insight-is-the-newest-mars-weather-service/"
    browser.visit(url)

    time.sleep(5)

# following jupyter notebook annotation/code
    html = browser.html
    soup = BeautifulSoup(html, "html.paser")

    response = requests.get(url)
    header = soup.find('div', class_='content_title')
    title = header.find().text
    article = soup.find('div', class_='rollover_description_inner').text
    mars_data["headline"] = title
    mars_data["article"]

    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    twitter = "https://twitter.com/marswxreport?lang=en"
    twitter_request = requests.get(twitter)
    twitter_soup = BeautifulSoup(twitter_request.text, 'html.parser')
    tweet = twitter_soup.find('div', class_="js-tweet-text-container")
    mars_weather = tweet.text
    mars_data["weather"] = mars_weather

    facts_url = 'https://space-facts.com/mars/'
    facts = pd.read_html(facts_url)
    df = facts[0]
    df=df.rename(columns={0:"Description", 1:"Value"})
    html_table = df.to_html(index=False)
    html_table.replace('\n', '')
    df.to_html('table.html')
    mars_data["facts"] = html_table

    hemispheres_url = 'https://astrogeology.usgs.gov'
    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, 'html.parser')
    items = soup.find_all('div', class_='item')
    hemisphere_image_urls = []  

    browser.quit()
    
    return mars_data

