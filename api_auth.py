import tweepy
from decouple import config

def create_api(
    CONSUMER_KEY=None, 
    CONSUMER_SECRET=None,
    ACCESS_TOKEN=None, 
    ACCESS_TOKEN_SECRET=None
    ):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    try:
        api = tweepy.API(auth)
        api.verify_credentials()
        return api
    except Exception as e:
        raise e


create_api(
    config("CONSUMER_KEY"),
    config("CONSUMER_SECRET"),
    config("ACCESS_TOKEN"),
    config("ACCESS_TOKEN_SECRET")
    )
    