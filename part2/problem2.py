import requests
import xml.etree.ElementTree as ET

############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############


google_news_url="https://news.google.com/news/rss"

def get_response_content(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.content

def get_headlines(rss_url):
    """
    @returns a list of titles from the rss feed located at `rss_url`
    """
    xml = get_response_content(rss_url)

    root = ET.fromstring(xml)

    headlines = []

    for item in root.findall(".//item"):
        title = item.find("title").text
        headlines.append(title)

    return headlines



for headline in get_headlines(google_news_url):
    print(headline)