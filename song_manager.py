from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from song import Song


class SongManager:
    """
    The SongManager class is responsible for coordinating all transactions
    between the higher level programs that use the data, and the actual
    database. Since each transaction is one of the crud operations (create,
    read, update, delete) we provide methods for each of these techniques.

    The class basically just reads and writes data to the database. The
    constructor sets up the initial connection (student object <-> database)
    and each of the other methods performs an autonomous transaction (ie:
    open db session, interact with db, commit changes, close session.
    """

    def __init__(self, song_db):
        """ Creates a Song object and map to the Database """

        if song_db is None or song_db == "":
            raise ValueError(f"Song database [{song_db}] not found")

        engine = create_engine('sqlite:///' + song_db)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_song(self, new_song: Song):
        """ Adds a new song to the song database """

        if new_song is None or not isinstance(new_song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()
        session.add(new_song)

        session.commit()

        song_id = new_song.song_id
        session.close()

        return song_id

    def update_song(self, song):
        """ Update existing song to match song_upd """
        if song is None or not isinstance(song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()

        existing_song = session.query(Song).filter(
                Song.file_location == song.file_location).first()
        if existing_song is None:
            raise ValueError(f"Song {song.title} does not exist")

        existing_song.album = song.album
        existing_song.genre = song.genre
        existing_song.rating = song.rating
        existing_song.last_played = song.last_played
        existing_song.play_count = song.play_count

        session.commit()
        session.close()

    def get_song(self, file_location):
        """ Return song object matching file location"""
        if file_location is None or type(file_location) != str:
            raise ValueError("Invalid file_location")

        session = self._db_session()

        song = session.query(Song).filter(
                Song.file_location == file_location).first()

        session.close()

        return song

    def delete_song(self, file_location):
        """ Delete a song from the database """

        if file_location is None or type(file_location) != str:
            raise ValueError("Invalid Song URL")

        session = self._db_session()

        song = session.query(Song).filter(
                Song.file_location == file_location).first()
        if song is None:
            session.close()
            raise ValueError("Song does not exist")

        session.delete(song)
        session.commit()

        session.close()

    def get_all_songs(self):
        """ Return a list of all songs in the DB """
        session = self._db_session()

        all_songs = session.query(Song).all()

        session.close()

        return all_songs
