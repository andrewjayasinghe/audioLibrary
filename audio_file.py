from datetime import datetime
import os
from abc import abstractmethod
from sqlalchemy import Column, Text, Integer
from base import Base


class AudioFile(Base):
    """Represents an abstract audio file

    Author: Harish Anantharajah
    ID: A01054991
    Date: January 31th, 2020
    """

    __tablename__ = "song_tbl"
    song_id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    artist = Column(Text, nullable=False)
    file_location = Column(Text, nullable=False)
    runtime = Column(Text)
    date_added = Column(Text, nullable=False)
    play_count = Column(Integer, nullable=False)
    last_played = Column(Text)
    rating = Column(Integer)

    _DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, title: str, artist: str, runtime: str, file_location: str):
        """Initializes a new audio file"""
        if type(title) is str and type(artist) is str:
            self.title = title
            self.artist = artist
        else:
            raise ValueError("title and artist must be a string")

        self.runtime = runtime

        if AudioFile.__valid_filename(file_location):
            self.filename = os.path.basename(file_location)
            self.pathname = os.path.dirname(file_location)
        else:
            raise FileNotFoundError("file_location not found")

        self.rating = 0

        self.date_added = datetime.now().strftime(AudioFile._DATE_FORMAT)

        self.play_count = 0
        self.last_played = None

    @abstractmethod
    def get_description(self) -> str:
        pass

    def get_location(self) -> (str, str):
        """retuns the filename and pathname"""
        return self.filename, self.pathname

    @abstractmethod
    def meta_data(self) -> str:
        pass


    @property
    def get_date_added(self):
        """ return the date the song or playlist was added to the library """
        return self.date_added

    @property
    def get_last_played(self):
        """ return the date the song or playlist was last played """
        if self.last_played is None:
            return None
        else:
            return self.last_played.strftime(AudioFile._DATE_FORMAT)

    @property
    def get_play_count(self):
        """ return the number of times the song or playlist has been played """
        return self.play_count

    def increment_usage_stats(self):
        """ update the play count and last played time when a song is played """
        self.play_count += 1
        self.last_played = datetime.now()

    @classmethod
    def __valid_datetime(cls, date):
        """ private method to validate the date is datetime object """
        if type(date) is not datetime:
            return False
        else:
            return True

    @classmethod
    def __valid_time(cls, runtime):
        try:
            datetime.strptime(runtime, "%M:%S")
            return True
        except ValueError:
            return False

    @classmethod
    def __valid_filename(cls, filename):
        if os.path.isfile(filename):
            return True
        else:
            return False
