from tweepy.streaming import StreamListener
from src.DataHandler.base import DataHandler
from tweepy import API


class BaseListener(StreamListener):
    """ This is a son of StreamListener from tweepy. Will allow us to treat
        tweets in a customized way.

        Attributes
        ----------

        api:
            a tweepy API connection e.g.
            API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            use the above to avoid error 420 (too many calls to Twitter API)

        datahandler:
            An object of the class DataHandler to store the data where we want

        cleaner:
            a function that takes the original mined tweed and transforms it to another JSON file


        Methods
        -------
        save:
            save data on the current file
        """

    def __init__(self, api: API, datahandler: DataHandler, cleaner):

        self.datahandler = datahandler
        self.cleaner = cleaner
        StreamListener.__init__(self, api=api)

    def on_data(self, data):
        data = self.cleaner(data)
        self.datahandler.save(data)

    def on_error(self, status):
        print("Twitter error code: {}".format(status))

