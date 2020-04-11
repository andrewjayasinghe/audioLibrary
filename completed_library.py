from podcast import Podcast
from song import Song
from PlayList import PlayList
import eyed3
import os


class AudioLibrary:
    '''This is a class for the Audio Library'''
    def __init__(self):
        '''This function is the constructor'''
        self._songs = []
        self._podcasts = []
        self._playlists = []

    # ********************SONG******************** #

    def add_song(self, song: Song)->None:
        '''This method is for adding a song to the list'''
        if isinstance(song, Song):
            self._songs.append(song)
        else:
            raise ValueError("song added must be type Song")

    def remove_song(self, song)->None:
        '''This method is for removing a song from the list'''
        if isinstance(song, Song):
            self._songs.remove(song)
        elif isinstance(song, int):
            if song > len(self._songs):
                raise IndexError("parameter is out of range")
            else:
                self._songs.pop(song - 1)
        else:
            raise ValueError("remove song by Song object or number")

    def search_song(self, title: str = None, artist: str = None, album: str = None)->int:
        """ Returns the index position of a specified song"""
        a = []
        index = -1
        counter = 0

        for song in self._songs:
            if song.meta_data()["title"] == title:
                a.append(self._songs.index(song))
            if song.meta_data()["artist"] == artist:
                a.append(self._songs.index(song))
            if song.meta_data()["album"] == album:
                a.append(self._songs.index(song))

        for i in a:
            if a.count(i) > counter:
                counter = a.count(i)
                index = i

        if index != -1:
            return index + 1

    @property
    def get_songs(self)->list:
        '''This is a getter for the song list'''
        return self._songs

    def list_songs(self) -> list:
        '''This method is for printing the songs in the library with proper formatting'''
        formatted_songs = []
        index = 0
        for song in self._songs:
            index += 1
            meta = song.meta_data()
            s = "{}. {} {} {} {}".format(index, meta["title"].ljust(20), meta["artist"].ljust(20),
                                         meta["album"].ljust(20), meta["runtime"])
            formatted_songs.append(s)
        return formatted_songs

    def titles(self):
        list = []
        for song in self._songs:
            song_info = song.meta_data()
            song_title = song_info["title"]
            list.append(song_title)
        return list

    def get_song(self,title):
        count = 0
        while count < len(self._songs):
            song_info = self._songs[count].meta_data()
            song_title = song_info["title"]
            if song_title == title:
                return self._songs[count]
            else:
                count += 1

    def get_song_info(self, pos: int)->str:
        '''This method is for returning the description of a specified song'''
        AudioLibrary._validate_int("position", pos)
        if pos > len(self._songs):
            raise IndexError("position is out of range")
        else:
            return self._songs[pos - 1].get_description()

    # ********************PODCAST******************** #

    def add_podcast(self, podcast: Podcast)->None:
        '''This method is for adding a podcast'''
        if isinstance(podcast, Podcast):
            self._podcasts.append(podcast)
        else:
            raise ValueError("podcast added must be type Podcast")

    def remove_podcast(self, podcast)->None:
        '''This method is for removing a podcast from the pocast list'''
        if isinstance(podcast, Podcast):
            self._podcasts.remove(podcast)
        elif isinstance(podcast, int):
            self._podcasts.pop(podcast - 1)
        else:
            raise ValueError("remove podcast by Podcast object or number")

    @property
    def get_podcasts(self)->list:
        '''This method is for getting the podcast list'''
        return self._podcasts

    def list_podcasts(self) -> list:
        '''This method formats the podcasts and puts them into a list that can be accessed to print properly formatted podcasts'''
        formatted_podcasts = []
        index = 0
        for podcast in self._podcasts:
            meta = podcast.meta_data()
            index += 1
            s = f"{index}. {str(meta['series']).ljust(20)} {str(meta['title']).ljust(40)} {str(meta['runtime'])}"
            formatted_podcasts.append(s)
        return formatted_podcasts

    def search_podcast(self, title: str = None, artist: str = None, series: str = None)->int:
        """ Returns the index position of a specified song"""
        a = []
        index = -1
        counter = 0

        for podcast in self._podcasts:
            meta = podcast.meta_data()
            if meta["title"] == title:
                a.append(self._podcasts.index(podcast))
            if meta["artist"] == artist:
                a.append(self._podcasts.index(podcast))
            if meta["series"] == series:
                a.append(self._podcasts.index(podcast))

        for i in a:
            if a.count(i) > counter:
                counter = a.count(i)
                index = i

        if index != -1:
            return index + 1

    def get_podcast_info(self, pos: int)->None:
        '''This method returns the description of a podcast'''
        AudioLibrary._validate_int("position", pos)
        if pos > len(self._playlists):
            raise IndexError("position is out of range")
        else:
            return self._podcasts[pos - 1].get_description()

    # ********************PLAYLIST******************** #

    def add_playlist(self, playlist: PlayList)->None:
        '''This method adds a playlist to the playlist list'''
        if isinstance(playlist, PlayList):
            self._playlists.append(playlist)
        else:
            raise ValueError("playlist added must be type PlayList")

    def remove_playlist(self, playlist)->None:
        '''This method is for removing a playlist from the library'''
        if isinstance(playlist, PlayList):
            self._playlists.remove(playlist)
        elif isinstance(playlist, int):
            self._playlists.pop(playlist - 1)
        else:
            raise ValueError("remove playlist by PlayList object or number")

    def list_playlists(self) -> list:
        '''This method is for formatting the playlists in the playlist for printing'''
        formatted_playlists = []
        index = 0
        for playlist in self._playlists:
            index += 1
            meta = playlist.meta_data()
            s = "{}. {} {} # of songs: {}".format(index, meta["name"].ljust(20), meta["desc"].ljust(40),
                                                  len(meta["songs"]))
            formatted_playlists.append(s)
        return formatted_playlists

    def make_playlist(self, name, desc)->None:
        '''This method is for making a playlist Object'''
        AudioLibrary._validate_str("name", name)
        AudioLibrary._validate_str("description", desc)
        self._playlists.append(PlayList(name, desc))

    def add_song_playlist(self, pl_num: int, song_num: int)->None:
        '''This method is for adding a song to a playlist'''
        AudioLibrary._validate_int("playlist number", pl_num)
        AudioLibrary._validate_int("song number", song_num)
        if pl_num > len(self._playlists) or song_num > len(self._songs):
            raise IndexError("parameter out of range")
        else:
            self._playlists[pl_num - 1].add_song(self._songs[song_num - 1])

    def list_songs_playlist(self, pos: int) -> list:
        '''This method is for formatting the playlist songs to a printable version'''
        AudioLibrary._validate_int("position", pos)
        formatted_playlist_songs = []
        index = 0
        for song in self._playlists[pos - 1].meta_data()["songs"]:
            meta_song = song.meta_data()
            index += 1
            s = "{}. {} {} {} {}".format(index, meta_song["title"].ljust(20), meta_song["artist"].ljust(20),
                                         meta_song["album"].ljust(20), meta_song["runtime"])
            formatted_playlist_songs.append(s)
        return formatted_playlist_songs

    def remove_song_playlist(self, pl_num: int, song_num: int)->None:
        '''This method is for removing a song from a playlist'''
        AudioLibrary._validate_int("playlist number", pl_num)
        AudioLibrary._validate_int("song number", song_num)
        if pl_num > len(self._playlists) or song_num > len(self._songs):
            raise IndexError("parameter out of range")
        else:
            self._playlists[pl_num - 1].remove_song(self._songs[song_num - 1])

    @property
    def get_playlists(self)->list:
        '''this is a getter for all the playlists in the library'''
        return self._playlists

    # ********************OTHER******************** #

    def load(self)->None:
        '''This method is for loading a song into the Audio Player for playing'''
        dir = os.path.join(os.getcwd(), "music")
        files = os.listdir(dir)
        for file in files:
            if file.find(".mp3") != -1:
                filepath = os.path.join(dir, file)
                mp3_file = eyed3.load(filepath)
                seconds = int(mp3_file.info.time_secs)
                runtime = str(seconds // 60) + ":" + str(seconds % 60)
                self._songs.append(Song(title=str(getattr(mp3_file.tag, "title")),
                                        artist=str(getattr(mp3_file.tag, "artist")),
                                        runtime=runtime,
                                        album=str(getattr(mp3_file.tag, "album")),
                                        filepath=filepath))
                                        # genre=str(getattr(mp3_file.tag, "genre")),


    @staticmethod
    def _validate_str(param, str_value)->None:
        '''This private method is for validating all string parameters in the calss'''
        if not isinstance(str_value, str):
            raise ValueError(param + "must be a string")

    @staticmethod
    def _validate_int(param, int_value)->None:
        '''This private method is for validating all Integer parameters in the calss'''
        if not isinstance(int_value, int):
            raise ValueError(param + "must be an integer")



