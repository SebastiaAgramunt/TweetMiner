from dotenv import load_dotenv
import os
load_dotenv(verbose=True)



# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API


API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")


tracklist = ['#Brexit', '#brexit', '#br']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 10

# Create the class that will handle the tweet stream
'''
class StdOutListener(StreamListener):

    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)
'''
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)

    def on_error(self, status):
        print(status)


# Handles Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
'''
listener = StdOutListener(StdOutListener(api))
stream = Stream(auth, listener)
stream.filter(track=tracklist)
'''
#trends_result = api.trends_place(1)
#trends_result = api.trends_closest(lat=41.390205, long=2.154007)
import json
#trends = api.trends_place(id=753692)
#print(json.dumps(trends))
print(json.dumps(api.trends_available()))
#for trend in trends_result[0]["trends"]:
#    print(trend["name"])