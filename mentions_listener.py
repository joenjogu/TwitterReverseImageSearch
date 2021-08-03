import tweepy
import api_auth

def get_mentions(api, count = 20):
    try:
        for status in tweepy.Cursor(api.mentions_timeline).pages(count):
            process_status(status)      
    except Exception as e:
        print(e)

def process_status(status):
    print(count(status))


api = api_auth.create_api()

get_mentions(api)