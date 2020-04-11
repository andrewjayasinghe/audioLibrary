import datetime
from datetime import datetime
import os
import typing
from usage_stats import UsageStats
from AudioFile import AudioFile


class Song(AudioFile):
    """Represents a song in the playlist
    Author: Andrew jayasinghe
    ID:A01016993
    rating needs setter and getter
    """

    def __init__(self, title: str, artist: str = None, runtime: str =None, filepath: str=None, album: str=None):
        """This method initializes the attributes"""
        super().__init__(title, artist, runtime, filepath)
        self._album = album
        self._genre = []
        self._one__genre_genre = None

    def description(self) -> str:
        info = "{} by {} from the album {} added on {}. Runtime is {}. ".format(self._title, self._artist, self._album,
                                                                                self._date_added, self._runtime)
        if self._usage.play_count != 0 :
            info += "Play count is {}. Last played on: {} ".format(self._usage.play_count, self._usage.last_played)

        return info

    def meta_data(self):

        keys = ['title', 'artist', 'album', 'date_added', 'runtime', "pathname", 'filename', 'play_count',
                'rating', 'last played', "Genre"]
        values = [self._title, self._artist, self._album, self._date_added, self._runtime, self._path, self._file,
                  self._usage.play_count, self._user_rating, self._usage.last_played, self._genre]
        my_dict = dict(zip(keys, values))
        return my_dict

    def set_genre(self):
        gen = input("enter a genre: ")
        if "," in gen:
            new = gen.split(",")
            for i in new:
                self._genre.append(i)
        else:
            print("do you want to add more stuff?")

    def display_genre(self):
        list =[]
        for i in self._genre:
            list.append(i)
        return list

    @property
    def music_genre(self):
        return self._one__genre

    @music_genre.setter
    def music_genre(self,value):
        self._one__genre = value
        if "," in self._one__genre and type(self._one__genre) is str:
            gen = self._one__genre.split(",")
            for i in gen:
                self._genre.append(i)
        else:
            print('please enter good stuff')

    def get_location(self):
        return self._filepath