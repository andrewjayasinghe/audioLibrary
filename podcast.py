import datetime
import os
import typing
from usage_stats import UsageStats
from AudioFile import AudioFile
from datetime import time


class Podcast(AudioFile):
    """Represents a song in the playlist
    Author: Andrew jayasinghe
    ID:A01016993
    rating needs setter and getter
    """

    def __init__(self, title: str, artist: str, runtime: str, filepath: str, series: str, season: str = None,
                 episode_number: int = None):
        """This method initializes the attributes"""
        super().__init__(title, artist, runtime, filepath)
        self._series = series
        self._season = season
        self._episode_number = episode_number
        self._episode_date = datetime.date.today()
        self._progress = time(0,0)

    def description(self) -> str:
        """and it came to pass that thus is the function that is the creator of eternal descriptions"""
        info = "{}: {}, {}".format(self._series, self._title,
                                   self._episode_date)
        if self._season is not None:
            info += ", Season {}".format(self._season)

        if self._episode_number is not None:
            info += ", Episode {}".format(self._episode_number)

        minute,second = self._runtime.split(":")
        display_runtime = int(minute) + round(float(second) / 60)
        info += "({} mins)".format(display_runtime)

        return info

    @property
    def get_progress(self):
        return self._progress

    @get_progress.setter
    def get_progress(self, val):
        if type(val) is datetime.time:
            self._progress = val
        else:
            raise ValueError("The progress must be a datetime object")





    def meta_data(self):
        keys = ['title', 'artist', 'runtime', "pathname filename", 'Series', 'Season', "Episode Number",
                "Episode Date", "Episode Progress", 'last played', 'rating', 'play_count']
        values = [self._title, self._artist, self._runtime, self._filepath, self._series, self._season,
                  self._episode_number, self._date_added,
                  self._progress, self._usage.last_played, self._user_rating, self._usage.play_count]
        my_dict = dict(zip(keys, values))
        return my_dict
