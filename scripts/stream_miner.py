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
from config import ParseDataConfig

load_dotenv(verbose=True)

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")


if __name__ == "__main__":
    #getting config file
    config = ParseDataConfig.build_from_config()

    # Autenthication credentials for Twitter
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Twitter API definition and DataHandling object
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    f = FileHandler(config.tweets_filename, os.path.abspath(config.tweets_path))

    # Define the listener and the stream
    listener = BaseListener(api=api, datahandler=f, cleaner=clean)
    stream = Stream(auth, listener)
    stream.filter(track=config.tracklist)
