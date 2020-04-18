import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import vlc
from datetime import datetime


class PlayQueueWindow(tk.Frame):

    def __init__(self, parent, my_controller):
        """ Initialize the popup queue window """
        tk.Frame.__init__(self, parent)

        self._songs_in_queue = []
        self.main_controller = my_controller

        self._vlc_instance = vlc.Instance()
        self._player = self._vlc_instance.media_player_new()

        self._current_title = None

        parent.title('Play Queue')

        self.top_frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)
        self.mid_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=10)
        self.bot_frame.grid(row=2, padx=30, pady=10)
        self.mid_frame.grid(row=1, padx=30, pady=10)

        self.song_listbox = tk.Listbox(self.top_frame, width=40,
                                       selectmode=tk.BROWSE)
        self.song_scrollbar = tk.Scrollbar(self.top_frame, orient='vertical')
        self.song_scrollbar.config(command=self.song_listbox.yview)
        self.song_listbox.config(yscrollcommand=self.song_scrollbar.set)

        self.details = tk.Label(self.mid_frame, text='')
        self.details.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        play_button = tk.Button(self.bot_frame, text='Play', width=10, bg="lightblue")
        play_button.grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
        play_button.bind("<Button-1>", self.do_play)

        stop_button = tk.Button(self.bot_frame, text='Stop', width=10, bg="lightblue")
        stop_button.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
        stop_button.bind("<Button-1>", self.do_stop)

        remove_button = tk.Button(self.bot_frame, text='Remove', width=10, bg="red")
        remove_button.grid(row=2, column=1, sticky=tk.E, padx=20, pady=5)
        remove_button.bind("<Button-1>", self.do_remove)

        pause_button = tk.Button(self.bot_frame, text='Pause', width=10, bg="lightblue")
        pause_button.grid(row=1, column=0, sticky=tk.E, padx=20, pady=5)
        pause_button.bind("<Button-1>", self.do_pause)

        resume_button = tk.Button(self.bot_frame, text='Resume', width=10, bg="lightblue")
        resume_button.grid(row=1, column=1, sticky=tk.E, padx=20, pady=5)
        resume_button.bind("<Button-1>", self.do_resume)

        skip_button = tk.Button(self.bot_frame, text='Skip', width=10, bg="lightblue")
        skip_button.grid(row=2, column=0, sticky=tk.E, padx=20, pady=5)
        skip_button.bind("<Button-1>", self.do_next)

        self.song_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.song_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



    def add_song_to_queue(self, song):
        """ Adds song to the queue"""
        song_display = f'{song["title"]} - {song["artist"]}'
        self._songs_in_queue.append(song)
        self.song_listbox.insert(tk.END, song_display)

    def do_play(self, event):
        """Play a song specified by index. """
        self.index = self.song_listbox.index(tk.ACTIVE)

        if len(self._songs_in_queue) == 0:
            msg_str = 'No songs loaded on to the song Que'
            messagebox.showinfo(title='Play Error', message=msg_str)
            return

        song = self._songs_in_queue[self.index]
        song["play_count"] += 1
        song["last_played"] = datetime.now().strftime("%Y-%m-%d")

        self.details["text"] = f'Last Played: {song["last_played"]}   Count: {song["play_count"]}'
        file_path = song["file_location"]
        media = self._vlc_instance.media_new_path(file_path)
        self._player.set_media(media)
        self._player.play()

        self.main_controller.update_play(song)


    def do_pause(self, event):
        """ Pause the player """
        if self._player.get_state() == vlc.State.Playing:
            self._player.pause()

    def do_resume(self, event):
        """ Resume playing """
        if self._player.get_state() == vlc.State.Paused:
            self._player.pause()

    def do_stop(self, event):
        """ Stop the player """
        self._player.stop()

    def do_remove(self, event):
        """ Remove song from the player """
        index = self.song_listbox.index(tk.ACTIVE)
        self._player.stop()
        self.song_listbox.delete(index)
        self._songs_in_queue.pop(index)

    def do_next(self, event):
        """ Plays next song in the queue"""
        self.index += 1
        if self.index + 1> len(self._songs_in_queue):
            messagebox.showinfo(title='Next', message="No New Songs in Queue")
            return

        song = self._songs_in_queue[self.index]
        song["play_count"] += 1
        song["last_played"] = datetime.now().strftime("%Y-%m-%d")

        self.details["text"] = f'Last Played: {song["last_played"]}   Count: {song["play_count"]}'
        file_path = song["file_location"]
        media = self._vlc_instance.media_new_path(file_path)
        self._player.set_media(media)
        self._player.play()

        self.main_controller.update_play(song)

