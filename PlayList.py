import datetime
import os
import typing
from usage_stats import UsageStats
from song import Song
from collections import Counter
from abc import abstractclassmethod


class PlayList:
    """Represents a song in the playlist
    Author: Andrew jayasinghe
    ID:A01016993
    playlist name should have a setter and a getter
    """

    def __init__(self, name: str, description: str, ):
        """This method initializes the attributes"""
        if type(name) is str and type(description) is str:
            self._name = name
            self._description = description
        else:
            raise ValueError("Type of name and description is not a string")
        self._playlist = []
        self._usage = UsageStats(datetime.date.today())
        self._date_added = self._usage.date_added
        self._play_count = self._usage.play_count

    def add_song(self, song=Song, position: int = None):
        """This method adds a song to the playlist and the position of the song may be entered as well"""
        if position is None:
            self._playlist.append(song)
        else:
            if type(position) is int and position <= len(self._playlist):
                self._playlist.insert(position, song)
            else:
                raise ValueError("Index is out of range")


    def remove_song(self, song):
        """This method removes a song from the playlist"""
        if song in self._playlist:
            self._playlist.remove(song)
        else:
            raise ValueError("Song does not exist in the Playlist")

    def move_song(self, song, new_position=None):
        """This method moves the play que of the playlist"""
        if new_position is None:
            raise ValueError("please enter the new position of the song")
        else:
            if type(new_position) is int:
                if new_position < len(self._playlist) and song in self._playlist:
                    old_index = self._playlist.index(song)
                    self._playlist.insert(new_position, self._playlist.pop(old_index))
                else:
                    raise ValueError("Index out of range or Song does not exist. please double check your values")

    def list_song(self) -> list:
        """This method returns a list of details of the songs in the playlist"""
        list = []
        index = 0
        for song in self._playlist:
            index += 1
            value = song.meta_data()
            details = "{}. {} {} {} {}".format(index, value["title"].ljust(20), value["artist"].ljust(20),
                                               value["album"].ljust(20), value["runtime"].ljust(20))
            list.append(details)
        return list

    @property
    def playlist_description(self):
        '''Gets the play list description'''
        return self._description

    @playlist_description.setter
    def playlist_description(self, description):
        '''This method changes the playlist description according to user preference'''
        self._description = description

    @property
    def playlist_name(self):
        '''Gets the name of the playlist'''
        return self._name

    @playlist_name.setter
    def playlist_name(self, new_name):
        '''changes the name of the playlist'''
        self._name = new_name

    @property
    def play_count(self) -> (int):
        """This method counts how many times the song was played and its also gives the last date it was played."""
        return self._play_count()

    def update_usage_stats(self) -> int:
        return self._usage.increment_usage_stats()

    def usage_data(self):
        '''This method gives the usage data'''
        information = "The playlist was created on {} ".format(self._date_added)
        if PlayList.play_count:
            information += "Play count is {}. Last played on: {} ".format(self._play_count,self._usage.last_played)
        return information

    @property
    def update_play_count(self):
        """This method counts how many times the song was played and its also gives the last date it was played."""
        return self._play_count()

    def usage_stats(self):
        return self._usage.increment_usage_stats()

    def find_song(self, title=None, artist=None, album=None):
        """This method is yoused to search for a song in the playlist"""
        D = []

        if title is not None or album is not None or artist is not None:
            for song in self._playlist:
                if song._title==title:
                    D.append(self._playlist.index(song))
                if song._artist== artist:
                    D.append(self._playlist.index(song))
                if song._album== album:
                    D.append(self._playlist.index(song))
            occurence_count = Counter(D)
            most_counted = occurence_count.most_common(1)[0][0]
            return most_counted


    def number_of_songs(self):
        '''This returns the total number of songs in the playlist'''
        number = "There are {} songs in the playlist".format(len(self._playlist))
        return number

    def get_song_by_position(self, position=None):
        '''This method gets a song based on its position on the playlist que'''
        list = []
        if position is None:
            return "please enter the required position"
        else:
            if type(position) is int and position < len(self._playlist):
                for song in self._playlist:
                    value = song.meta_data()
                    details = " {} {} {} {}".format(value["title"].ljust(20), value["artist"].ljust(20),
                                                    value["album"].ljust(20), value["runtime"].ljust(20))
                    list.append(details)
                return list[position]
            else:
                raise ValueError("The specific position does not exist in the playlist")