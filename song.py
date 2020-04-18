from audio_file import AudioFile
# from usage_stats import UsageStats
# from datetime import datetime
from sqlalchemy import Column, Text
from base import Base
from datetime import datetime


class Song(AudioFile):

    album = Column(Text)
    genre = Column(Text)

    def __init__(self, title: str, artist: str, runtime: str, file_location: str,
                 album: str, genre: str = None):
        super().__init__(title, artist, runtime, file_location)
        if type(album) is str:
            self.album = album
        else:
            raise ValueError("album name must be a string")

        if genre is not None:
            self.genre = genre
        self.file_location = file_location

    def get_description(self) -> str:
        """Returns description of a song"""
        desc = "{} by {} from the album {} added on {}. Runtime is {}. "\
            .format(self.title, self.artist, self.album, self.usage_stats.date_added, self.runtime)
        if self.usage_stats.last_played is not None:
            desc += "Last played on {}. ".format(self.usage_stats.last_played)
        if self.rating != "" and self._usage_stats.last_played is not None:
            desc += "User rating is {}.".format(self.rating)
        return desc

    def get_location(self):
        return self.file_location

    @property
    def get_runtime(self):
        return self.runtime

    def meta_data(self) -> dict:
        data = {"title": self.title, "artist": self.artist, "album": self.album,
                "date_added": self.date_added, "runtime": self.runtime, "file_location": self.file_location,
                "rating": self.rating, "genre": self.genre, "last_played": self.last_played, "play_count": self.play_count}
        return data
