import tweepy

def create_api(
    consumer_key = "LbBE7LfWgAH1vWTZFacztjNJx", 
    consumer_secret = "dxIoZwPvFKx8cWG9azjNVEktCF9VNuLwpKuSOtEJJvqp3Qb0KF", 
    access_token = "1678385940-JiQ6Uaas6RJ4CRNSnHd8hWTUayx9qIHwTIP2DX2", 
    access_token_secret = "lfCcxV7Y9enNjLeFGzhFC5J58KDjGIQJP8OobjbnwojH1"
    ):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:
        api = tweepy.API(auth)
        api.verify_credentials()
        return api
    except Exception as e:
        raise e


create_api(
    "LbBE7LfWgAH1vWTZFacztjNJx",
    "dxIoZwPvFKx8cWG9azjNVEktCF9VNuLwpKuSOtEJJvqp3Qb0KF", 
    "1678385940-JiQ6Uaas6RJ4CRNSnHd8hWTUayx9qIHwTIP2DX2", 
    "lfCcxV7Y9enNjLeFGzhFC5J58KDjGIQJP8OobjbnwojH1"
    )