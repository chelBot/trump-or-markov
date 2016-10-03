import sys
import operator
import requests
import json
import twitter


twitter_consumer_key = 'cGKH2KZE3togQPJysyKP7lwt1'
twitter_consumer_secret = 'TmviRie72WEnlHuDDDhKgzBDthjKkra1KhUIlerhT1SLvskPrZ'
twitter_access_token = '4441574236-XCw1c2PSVrXDyfHFsKO8jAfTUS6qaMZCbmOrdFV'
twitter_access_secret = 'dkO2cRh6FMfJAP2Wx1cUga7L8JS5P5LpcmXCBUFvv1vdK'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

handle = "@realDonaldTrump"

statuses = twitter_api.GetUserTimeline(screen_name=handle, count=20000, include_rts=False)

for status in statuses:
    print status.text
