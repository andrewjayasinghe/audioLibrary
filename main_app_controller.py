import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from chooser_window import ChooserWindow
from songlist_window import SonglistWindow
from song_details_window import SongDetailsWindow
from play_queue_window import PlayQueueWindow
import os
import requests
from song import Song
import csv
import eyed3
from datetime import datetime

class MainAppController(tk.Frame):
    """ Main Application Window """
    def __init__(self, parent):
        """ Create the views """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._chooser = ChooserWindow(self._root_win, self)
        self._play_queue = None


    def quit_callback(self):
        """ Exit the application. """
        self.master.quit()


    def openfile(self):
        """ Load the song from the file """
        new_file = askopenfilename(filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*"))).replace('/', '\\')
        mp3_file = eyed3.load(new_file)
        seconds = int(mp3_file.info.time_secs)
        runtime = str(seconds // 60) + ":" + str(seconds % 60)
        song_data = {"title": str(getattr(mp3_file.tag, "title")),
                                "artist": str(getattr(mp3_file.tag, "artist")),
                                "runtime": runtime,
                                "album": str(getattr(mp3_file.tag, "album")),
                                "genre": str(getattr(mp3_file.tag, "genre")),
                                "file_location": new_file}

        response = requests.post("http://localhost:5000/song", json=song_data)
        if response.status_code == 200:
            msg_str = f'{str(getattr(mp3_file.tag, "title"))} added to the database'
            messagebox.showinfo(title='Open Song', message=msg_str)


    def add_callback(self, event):
        """ Save a new song name to the file. """
        URL = self._chooser.get_url()

        if URL == "" or URL[-4:] != ".mp3":
            messagebox.showerror(title='Invalid URL Entry', message='URL must be a local mp3 file')
            return

        mp3_file = eyed3.load(URL)
        seconds = int(mp3_file.info.time_secs)
        runtime = str(seconds // 60) + ":" + str(seconds % 60)
        song_data = {"title": str(getattr(mp3_file.tag, "title")),
                     "artist": str(getattr(mp3_file.tag, "artist")),
                     "runtime": runtime,
                     "album": str(getattr(mp3_file.tag, "album")),
                     "genre": str(getattr(mp3_file.tag, "genre")),
                     "file_location": URL}

        self._chooser.clear_url()

        response = requests.post("http://localhost:5000/song", json=song_data)
        if response.status_code == 200:
            msg_str = f'{str(getattr(mp3_file.tag, "title"))} added to the database'
            messagebox.showinfo(title='Add Song', message=msg_str)

    def delete_callback(self, event):
        """ Remove song from system. """
        URL = self._chooser.get_url()

        if URL == "" or URL[-4:] != ".mp3":
            messagebox.showerror(title='Invalid URL Entry', message='URL must be a local mp3 file')
            return

        mp3_file = eyed3.load(URL)

        self._chooser.clear_url()

        response = requests.delete("http://localhost:5000/song/" + URL)
        if response.status_code == 200:
            msg_str = f'{str(getattr(mp3_file.tag, "title"))} deleted from the database'
            messagebox.showinfo(title='Delete Song', message=msg_str)
            
    def update_callback(self, event):
        """ Update song info to the system. """
        song = self._song_details.updated_data()
        response = requests.put("http://localhost:5000/song/" + song["file_location"], json=song)
        self._song_details.destroy()
        if response.status_code == 200:
            msg_str = f'{song["title"]} updated to the database'
            messagebox.showinfo(title='Update Song', message=msg_str)


    def songlist_popup(self, event):
        """ Creates a new songlist window"""
        self._song_win = tk.Toplevel()
        self._songlist = SonglistWindow(self._song_win, self)
        response = requests.get("http://localhost:5000/song/all")
        song_list = [f'{s["title"]} - {s["artist"]}' for s in response.json()]
        self._songlist.set_songs(song_list)

    def song_details_popup(self, event):
        """ Creates a new song details edit window"""
        index = self._songlist.selected_listbox()
        response = requests.get("http://localhost:5000/song/all")
        selected_song = response.json()[index]
        self._song_details_win = tk.Toplevel()
        self._song_details = SongDetailsWindow(self._song_details_win, self, selected_song)

    def play_queue_popup(self, event):
        """ Creates a play queue window"""
        index = self._songlist.selected_listbox()
        response = requests.get("http://localhost:5000/song/all")
        selected_song = response.json()[index]
        self._play_queue_win = tk.Toplevel()
        self._play_queue = PlayQueueWindow(self._play_queue_win, self)
        self._play_queue.add_song_to_queue(selected_song)

    def add_to_queue(self, event):
        """ Add a song to the play queue listbox"""
        index = self._songlist.selected_listbox()
        response = requests.get("http://localhost:5000/song/all")
        selected_song = response.json()[index]

        self._play_queue.add_song_to_queue(selected_song)

    def update_play(self, song):
        """ Updates playcount and lastplayed to the database"""
        file_path = song["file_location"]
        requests.put("http://localhost:5000/song/" + file_path, json=song)


    def get_song_info(self, event):
        """ Gets the song info from the index of listbox"""
        index = self._songlist.selected_listbox()

        songs = requests.get("http://localhost:5000/song/all")

        selected_song = songs.json()[index]
        self._songlist.selected_song_info(selected_song)

    def search_song(self, event):
        """ Allows to search for keywords from selected attributes"""
        attributes = ("title", "artist", "album", "genre")
        searched_songs = []

        keyword = self._songlist.search_keyword()
        songs = requests.get("http://localhost:5000/song/all")

        if keyword != "":
            for song in songs.json():
                for attr in song:
                    if attr in attributes and keyword in song[attr]:
                        if song not in searched_songs:
                            searched_songs.append(song)
            song_list = [f'{s["title"]}' for s in searched_songs]
            self._songlist.set_songs(song_list)
        else:
            song_list = [f'{s["title"]}' for s in songs.json()]
            self._songlist.set_songs(song_list)




if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()
