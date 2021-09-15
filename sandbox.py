import tweepy
import logging
import api_auth
import Url_Retriever

logging = logging.basicConfig(level=logging.DEBUG)
api = api_auth.create_api()

# tweet = api.statuses_lookup([1280782192713531392])

# print (tweet[0])

# mentions = api.mentions_timeline()
HANDLED_STATUSES = set()
class MentionsStreamer(tweepy.StreamListener):
    def on_status(self, status):
        print(f"the tweet id is {status.id}")
        root_status_id = status.in_reply_to_status_id
        root_status = get_root_status(root_status_id)
        media_urls = get_media_urls(root_status_id)
        root_username = root_status.user.screen_name

        if media_urls:
            for url in media_urls:
                reverse_image_search(url)
                tweet_body = f"Hey! I think we found that image. \
                    Click the link below 👇 {url}"
                is_reply_successful = tweet_with_reply_option(
                    status_id=status.id,
                    tweet_body="get media url",
                    reply_username=root_username
                    )
                if is_reply_successful:
                    HANDLED_STATUSES.add(is_reply_successful)

        
    def on_error(self, status_code):
        print(f"got an error code: {status_code}")

def initialise_streamer():
    print("inside initialise_streamer")
    streamer = MentionsStreamer()
    print("created streamer")
    stream = tweepy.Stream(auth = api.auth, listener = streamer)
    print("initialised streamer")
    stream.filter(track = ['@joe_njogu'], is_async = True)
    print("streaming")

def get_root_status(status_id):
    root_status = api.get_status(status_id)

    return root_status

def get_media_urls(status):
    urls_getter = Url_Retriever.GetTweetMediaUrl(status)
    media_urls = urls_getter.get_media_url(status)
    media_urls_list = []
    if media_urls:
        media_urls_list.append(media_urls)
        return media_urls_list

def tweet_with_reply_option(status_id, tweet_body, reply_username=None):
    if reply_username:
        tweet_body = f"@{reply_username} {tweet_body}"
    try:
        status = api.update_status(status = tweet_body, in_reply_to_status_id = status_id)
        logging.debug(f"status updated with id {status.id}")
        return status.id

    except Exception as e:
        logging.error(f"status update failed with exception {e}")
        return None


initialise_streamer()
