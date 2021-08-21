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
        status_ids.append(tweet.in_reply_to_status_id)
    return status_ids
    
def get_media_urls(api, latest_status_ids):
    # print(latest_status_ids)
    flattened_status_ids = list(itertools.chain.from_iterable(latest_status_ids))
    status_objects = api.statuses_lookup(flattened_status_ids)
    print(status_objects)
    urls_getter = Url_Retriever.GetTweetMediaUrl(flattened_status_ids)

    status_media_urls = {}
    for tweet in status_objects:
        urls_list = []
        media_urls = urls_getter.get_media_url(tweet)
        if media_urls:
            # print(media_urls)
            urls_list.append(media_urls)
            new_dict = {tweet.id : urls_list}
            status_media_urls.update(new_dict)

    print(status_media_urls)

api = api_auth.create_api()
status_ids = get_mentions(api)
get_media_urls(api, status_ids)


# scheduler.start()
