import requests
import json
import lxml
from bs4 import BeautifulSoup
from datetime import datetime
from celery import shared_task
from . models import News

URL = 'https://news.ycombinator.com/rss'


@shared_task
def hackernews_rss():
    article_list = []

    try:
        print('Attention!! The scraping tool is starting')
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.find_all('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published_wrong = a.find('pubDate').text
            published = datetime.strptime(
                published_wrong, '%a, %d %b %Y %H:%M:%S %z')

            article = {
                'title': title,
                'link': link,
                'published': published,
                'source': 'HackerNews RSS'
            }
            article_list.append(article)
        print('Finished the scraping for the articles')

        return save_function(article_list)

    except Exception as e:
        print('The Scraping job failed. See exception: ')
        print(e)


@shared_task
def save_function(article_list):
    print('start saving')
    new_count = 0

    for article in article_list:

        try:
            News.objects.create(
                title=article['title'],
                link=article['link'],
                published=article['published'],
                source=article['source']
            )
            new_count += 1

        except Exception as e:
            print('failed')
            print(e)
            break

    return print('finished')
