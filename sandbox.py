import api_auth

api = api_auth.create_api()

# tweet = api.statuses_lookup([1280782192713531392])

# print (tweet[0])

mentions = api.mentions_timeline()

print(mentions)