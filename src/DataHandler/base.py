from abc import ABC, abstractmethod


class DataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save(self, data):
        pass