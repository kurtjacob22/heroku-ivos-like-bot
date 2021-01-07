import tweepy
import time
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = ['Blaster Silonga', 'Zild Benitez', 'Badjao de Castro', 'Unique Salonga', 'IV of Spades']


for x in range(len(search)):
    for tweets in tweepy.Cursor(api.search, search[x]).items():
        try:
            print("liked")
            tweets.favorite()
            time.sleep(1800)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    