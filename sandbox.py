import tweepy
import api_auth
import Url_Retriever

api = api_auth.create_api()

# tweet = api.statuses_lookup([1280782192713531392])

# print (tweet[0])

# mentions = api.mentions_timeline()

class MentionsStreamer(tweepy.StreamListener):
    def on_status(self, status):
        print(f"the tweet id is {status.id}")
        root_status_id = status.in_reply_to_status_id
        media_urls = get_media_urls(root_status_id)

        if media_urls:
            for url in media_urls:
                reverse_image_search()

        
    def on_error(self, status_code):
        print(f"got an error code: {status_code}")

def init():
    print("inside init")
    streamer = MentionsStreamer()
    print("created streamer")
    stream = tweepy.Stream(auth = api.auth, listener = streamer)
    print("initialised streamer")
    stream.filter(track = ['@joe_njogu'], is_async = True)
    print("streaming")

def get_media_urls(status_id):
    urls_getter = Url_Retriever.GetTweetMediaUrl(status_id)
    tweet = api.get_status(status_id)
    media_urls = urls_getter.get_media_url(tweet)
    media_urls_list = []
    if media_urls:
        media_urls_list.append(media_urls)
        return media_urls_list


init()
