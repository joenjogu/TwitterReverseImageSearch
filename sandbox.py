import tweepy
import logging
import api_auth
import url_retriever

logging.basicConfig(level=logging.DEBUG)
TRACK_TAG = "@FindImage"
HANDLED_STATUSES = set()
api = api_auth.create_api()


class MentionsStreamer(tweepy.StreamListener):
    def on_status(self, status):
        logging.debug(f"the tweet id is {status.id}")
        root_status_id = status.in_reply_to_status_id
        root_status = get_root_status(root_status_id)
        media_urls = get_media_urls(root_status)
        # root_username = root_status.user.screen_name

        if media_urls:
            for url in media_urls[0]:
                # reverse_image_search(url)
                logging.debug(f"chek this url out {url}")
                tweet_body = "Hey! I think we found that image."
                f"Click the link below 👇 to check it out {url}"
                is_reply_successful = tweet_or_reply(
                    status_id=status.id,
                    tweet_body=tweet_body,
                    reply_username=status.user.screen_name
                    )
                if is_reply_successful:
                    HANDLED_STATUSES.add(is_reply_successful)

    def on_error(self, status_code):
        logging.error(f"got an error code: {status_code}")


def initialise_streamer():
    streamer = MentionsStreamer()
    stream = tweepy.Stream(auth=api.auth, listener=streamer)
    logging.debug("initialised streamer")
    stream.filter(track=[TRACK_TAG], is_async=True)
    logging.debug("streaming")
    # stream.disconnect()


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


def tweet_or_reply(status_id, tweet_body, reply_username=None):
    if reply_username:
        tweet_body = f"@{reply_username} {tweet_body}"
    try:
        status = api.update_status(
            status=tweet_body,
            in_reply_to_status_id=status_id
            )
        logging.debug(f"status updated with id {status.id}")
        return status.id

    except Exception as e:
        logging.error(f"status update failed with exception {e}")
        return None


initialise_streamer()
