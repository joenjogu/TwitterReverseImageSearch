import tweepy
import api_auth
import Url_Retriever
import itertools
from apscheduler.schedulers.blocking import BlockingScheduler

HANDLED_STATUSES = set()
scheduler = BlockingScheduler()

# @scheduler.scheduled_job('interval', minutes=15)
def get_mentions(api, count = 20):
    proc_status_ids = []
    try:
        for status in tweepy.Cursor(api.mentions_timeline).pages(count):
            proc_status_ids.append(process_status(status))
        
        return proc_status_ids
    except Exception as e:
        raise (e)

def process_status(status):
    status_ids = []
    for tweet in status:
        in_reply_to_id = tweet.in_reply_to_status_id
        status_ids.append(in_reply_to_id)
        HANDLED_STATUSES.add(in_reply_to_id)
    return status_ids
    
def get_media_urls(api, latest_status_ids):
    # print(latest_status_ids)
    flattened_status_ids = list(itertools.chain.from_iterable(latest_status_ids))
    status_objects = api.statuses_lookup(flattened_status_ids)
    print(len(status_objects), len(flattened_status_ids))
    urls_getter = Url_Retriever.GetTweetMediaUrl(flattened_status_ids)

    status_media_urls = {}
    for tweet in status_objects:
        urls_list = []
        media_urls = urls_getter.get_media_url(tweet)
        if media_urls:
            # print(media_urls) 
            tweet_to_mention_link = []
            for status_id in flattened_status_ids:
                if tweet.id == status_id: tweet_to_mention_link = [status_id, tweet.id]

            urls_list.append(media_urls)
            new_dict = {tweet_to_mention_link : urls_list}
            status_media_urls.update(new_dict)

    print(status_media_urls)

api = api_auth.create_api()
status_ids = get_mentions(api)
get_media_urls(api, status_ids)


# scheduler.start()
