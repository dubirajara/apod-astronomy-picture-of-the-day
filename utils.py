from datetime import date

import requests
import redis
from decouple import config

redis_url = config('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)


def get_data():
    #if redis.get('date').decode("utf-8") != str(date.today()):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': config('API_KEY')}

    data = requests.get(url, params=payload).json()

    redis.set('date', data['date'])
    redis.set('title', data['title'])
    redis.set('image', data['hdurl'])
    redis.set('details', data['explanation'])

    data_content = {key.decode("utf-8"): redis.get(key).decode("utf-8") for key in redis.keys()}

    return data_content
