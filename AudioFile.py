import os
import abc
import typing
from usage_stats import UsageStats
from datetime import datetime
from datetime import date


class AudioFile:
    """Represents a song in the playlist
    Author: Andrew jayasinghe
    ID:A01016993
    rating needs setter and getter
    """

    def __init__(self, title: str, artist: str , runtime: str , filepath: str ):
        """This method initializes the attributes"""
        self._title = title
        self._artist = artist
        if AudioFile.validate_runtime(runtime):
            self._runtime = runtime
        self._user_rating = None
        self._filepath = filepath
        self._usage = UsageStats(date.today())
        self._date_added = self._usage.date_added
        self._play_count = self._usage.play_count
        if AudioFile._validate_filepath(self):
            self._file = os.path.basename(self._filepath)
            self._path = os.path.dirname(self._filepath)

    @abc.abstractmethod
    def description(self):
        pass

    def print_location(self) -> str:
        """This method shows the filename and the path of the song"""
        information = 'File name: {}   File path:{}'.format(self._file, self._path)
        return information


    @property
    def play_count(self):
        """This method counts how many times the song was played and its also gives the last date it was played."""
        return self._usage.play_count

    def update_usage_stats(self):
        return self._usage.increment_usage_stats()

    @staticmethod
    def _validate_filepath(self):
        """This method checks if the file actually exists and returns a boole value"""
        if os.path.exists(self._filepath):
            return True
        else:
            raise ValueError("the file does not exist")

    def _validate_user_rating(self):
        """This method checks to see if the user rating is blank or not."""
        if self._user_rating != None:
            return True
        else:
            print("No rating yet")
            return False

    @property
    def getter(self):
        return self._title, self._artist, self._runtime

    @property
    def user_rating(self):
        """This gets the user rating"""
        return self._user_rating

    @user_rating.setter
    def user_rating(self, value):
        """This assigns a value to the user rating"""
        self._user_rating = value

    @abc.abstractmethod
    def meta_data(self):
        pass

    @classmethod
    def validate_runtime(cls, time):
        try:
            if time is not None:
                datetime.strptime(time, "%M:%S")
                return True

        except ValueError:
            raise
