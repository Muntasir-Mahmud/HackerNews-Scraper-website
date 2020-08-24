from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hacker_news_scraper.settings')

app = Celery('hacker_news_scraper')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'scraping-task-one-min': {
        'task': 'scraping.tasks.hackernews_rss',
        'schedule': crontab(),
    },
}
