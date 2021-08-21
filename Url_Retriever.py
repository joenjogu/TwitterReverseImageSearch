import api_auth
import itertools
import time

class GetTweetMediaUrl():
    api = api_auth.create_api()

    def __init__(self, status_ids):
        self.status_ids = status_ids

    def get_tweet(self, status):
        try:
            tweet = self.api.get_status(status)
        except Exception as e:
            raise e
        return tweet

    def get_media_url(self, tweet):
        media_urls = []
        try:
            entities = tweet.extended_entities
            media_type = entities["media"][0]["type"]

            if media_type != "photo":
                pass
            else:
                try:
                    for key in range(len(entities["media"])):
                        photo_url = entities["media"][key]["media_url"]
                        if media_urls is not None: 
                            media_urls.append(photo_url)
                        
                except IndexError as e:
                    print ("Maximum photos reached...", e)
        except AttributeError as attribute_error: 
            print (f"tweet {tweet.id} has no media...", attribute_error)

        return media_urls 

    def get_urls(self):
        collective_urls = []
        start_time = time.clock()
        for status in self.status_ids:
            tweet = self.get_tweet(status)
            urls = self.get_media_url(tweet)
            collective_urls.append(urls)
        process_time = time.clock() - start_time
        print(f"Total process time {process_time} seconds\n")
        flattened_urls = list(itertools.chain.from_iterable(collective_urls))

        return flattened_urls