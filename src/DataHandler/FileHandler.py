from src.DataHandler.base import DataHandler
from src.utils import create_dirs
import os


class FileHandler(DataHandler):
    """ A class to handle files to write tweets

        Attributes
        ----------
        same as class src.DataHandler.base.DataHandler

        __filename:
            The name of the file we want to write

        __path:
            Path where we want to create the file, if it does not exist
            creates it.

        __rotate:
            boolean indicating if we want to rotate the file or not

        __maxsize:
            Max file size in bytes. Not used if rotate is False. Default is 100MB


        Methods
        -------
        save:
            save data on the current file
    """

    def __init__(self, filename, path, rotate=True,  maxsize=1e8):
        self.__filename = filename
        self.__path = path
        self.__maxsize = maxsize
        self.__rotate = rotate

        self.__i = 0
        create_dirs(path)

    def save(self, data):
        with open(self.__fname, 'a+') as file:
            file.write(data+'\n')
        if self.__rotate:
            self.__check_size()

    def __check_size(self):
        if os.stat(self.__fname).st_size > self.__maxsize:
            self.__i += 1

    @property
    def __fname(self):
        return self.__path + "/" + self.__filename + "_%0.2d" % self.__i
