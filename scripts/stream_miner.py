import sys
import os

# Execute this script from main directory "python scripts/stream_miner.py"
sys.path.append(os.path.abspath('.'))

from src.cleansing import clean
from dotenv import load_dotenv
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from src.Listener.base import BaseListener
from src.DataHandler.FileHandler import FileHandler

load_dotenv(verbose=True)

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")

# TODO: write a config file to put the tracklist
tracklist = ['#actnow', '#change', '#noplastic', '#environment', '#gogreen', '#saveourplanet',
             '#climatechange', '#eco', 'environment', '#fridaysforfuture', '#bethechange', '#plastic', 'methane',
             '#savetheworld', '#ecology', '#klimawandel', '#plasticpollution', '#sustainableliving', '#recycle',
             '#savetheearth', '#saveearth', '#plasticfree', '#savetheplanet', '#nature', '#globalwarming',
             '#noplanetb', '#climate', '#globalclimatestrike', 'artic', '#cleanenergy', '#zerowaste',
             '#gretathunberg', '#water', '#schoolstrike', '#ocean', '#green', '#climatechangeisreal', '#ecofriendly',
             '#climateaction', '#sustainable', '#sustainability', '#extinctionrebellion', '#renewableenergy',
             '#environmentalist', '#reuse', '#climateaction', '#pollution', '#climatejustice', '#carbon', '#ice',
             '#climateemergency', '#climatestrike', '#climatecrisis']


if __name__ == "__main__":

    # Autenthication credentials for Twitter
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Twitter API definition and DataHandling object
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # TODO: in the config file let it change the folder where we write
    f = FileHandler("tweets_", os.path.abspath("data/"))

    # Define the listener and the stream
    listener = BaseListener(api=api, datahandler=f, cleaner=clean)
    stream = Stream(auth, listener)
    stream.filter(track=tracklist)
