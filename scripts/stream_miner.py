import sys
import os

# Execute this script from main directory "python scripts/stream_miner.py"
sys.path.append(os.path.abspath('.'))

from src.cleansing import clean
from dotenv import load_dotenv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API


load_dotenv(verbose=True)

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")


tracklist = ['#actnow', '#change', '#noplastic', '#environment', '#gogreen', '#saveourplanet',
             '#climatechange', '#eco', 'environment', '#fridaysforfuture', '#bethechange', '#plastic', 'methane',
             '#savetheworld', '#ecology', '#klimawandel', '#plasticpollution', '#sustainableliving', '#recycle',
             '#savetheearth', '#saveearth', '#plasticfree', '#savetheplanet', '#nature', '#globalwarming',
             '#noplanetb', '#climate', '#globalclimatestrike', 'artic', '#cleanenergy', '#zerowaste',
             '#gretathunberg', '#water', '#schoolstrike', '#ocean', '#green', '#climatechangeisreal', '#ecofriendly',
             '#climateaction', '#sustainable', '#sustainability', '#extinctionrebellion', '#renewableenergy',
             '#environmentalist', '#reuse', '#climateaction', '#pollution', '#climatejustice', '#carbon', '#ice',
             '#climateemergency', '#climatestrike', '#climatecrisis']


class StdOutListener(StreamListener):

    def on_data(self, data):
        data = clean(data)
        print(data)

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    listener = StdOutListener(StdOutListener(api))
    stream = Stream(auth, listener)
    stream.filter(track=tracklist)
