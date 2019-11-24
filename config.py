import os
from configparser import ConfigParser, ExtendedInterpolation
from src.utils import project_abs_path

this_filepath = os.path.dirname(os.path.abspath(__file__))
config_path = this_filepath + '/config.ini'
tweet_config = ConfigParser(interpolation=ExtendedInterpolation())
tweet_config.read(config_path)

root_path = str(project_abs_path())


class ParseDataConfig:
    # A parser of the parameters in config.ini
    def __init__(self, tracklist, tweets_path, tweets_filename, rotate, maxsize):
        self.tracklist = tracklist
        self.tweets_path = tweets_path
        self.tweets_filename = tweets_filename
        self.rotate = rotate
        self.maxsize = maxsize

    @classmethod
    def build_from_config(cls, config: ConfigParser = tweet_config):

        tweets_path = config.get('writting_tweets', 'tweets_path')
        tweets_filename = config.get('writting_tweets', 'tweets_filename')
        rotate = config.getboolean('writting_tweets', 'rotate')
        maxsize = config.get('writting_tweets', 'maxsize')

        file_path = config.get('meta', 'tracklist_file')
        with open(file_path,'r') as file:
            tracklist = file.readlines()
            tracklist = [t.replace("\n", "").replace(" ", "") for t in tracklist]

        return cls(tracklist, tweets_path, tweets_filename, rotate, maxsize)


if __name__ == "__main__":
    config = ParseDataConfig.build_from_config()
    print(config.__dict__)