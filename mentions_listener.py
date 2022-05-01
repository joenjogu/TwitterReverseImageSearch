import itertools
from apscheduler.schedulers.blocking import BlockingScheduler
import tweepy
import api_auth
import url_retriever


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
        if (in_reply_to_id):
            original_and_mention_ids = [tweet.id, tweet.in_reply_to_status_id]
            HANDLED_STATUSES.add(original_and_mention_ids)
            # print(original_and_mention_ids)
    return HANDLED_STATUSES
    
def get_media_urls(api, latest_status_ids):
    urls_getter = url_retriever.GetTweetMediaUrl(flattened_status_ids)
    # flattened_status_ids = list(itertools.chain.from_iterable(latest_status_ids))
    # print(flattened_status_ids)
    # status_objects = api.statuses_lookup(flattened_status_ids)
    for lis in latest_status_ids:
        tweet = api.get_status(lis[0])
        urls_list = []
        media_urls = urls_getter.get_media_url(tweet)
        if media_urls:
            urls_list.append(media_urls)


    print(len(status_objects), len(flattened_status_ids))
    

    status_media_urls = {}
    for tweet in status_objects:
        urls_list = []
        media_urls = urls_getter.get_media_url(tweet)
        if media_urls:
            # print(media_urls) 
            tweet_to_mention_link = ""
            for status_id in flattened_status_ids:
                if tweet.id == status_id: tweet_to_mention_link = f"{status_id},{tweet.id}"

            urls_list.append(media_urls)
            new_dict = {tweet_to_mention_link : urls_list}
            status_media_urls.update(new_dict)

    print(status_media_urls)

api = api_auth.create_api()
status_ids = get_mentions(api)
get_media_urls(api, status_ids)


# scheduler.start()
