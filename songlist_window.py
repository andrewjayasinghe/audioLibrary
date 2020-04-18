import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

class SonglistWindow(tk.Frame):

    def __init__(self, parent, my_controller):
        """ Initialize the popup listbox window """
        tk.Frame.__init__(self, parent)

        self.song_info = ''

        parent.title('Song List')

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

        tk.Label(self.mid_frame, text='Filter:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.search = tk.Entry(self.mid_frame, width=20)
        self.search.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)


        song_details = tk.Button(self.bot_frame, text='Song Info', width=10, bg="lightblue")
        song_details.grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
        song_details.bind("<ButtonRelease-1>", my_controller.get_song_info)

        edit_details = tk.Button(self.bot_frame, text='Edit Info', width=10, bg="lightblue")
        edit_details.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
        edit_details.bind("<ButtonRelease-1>", my_controller.song_details_popup)

        search_song = tk.Button(self.mid_frame, text='Search', width=6, bg="lightgreen")
        search_song.grid(row=0, column=3, sticky=tk.E, padx=20, pady=5)
        search_song.bind("<ButtonRelease-1>", my_controller.search_song)

        play = tk.Button(self.bot_frame, text='Open Player', width=10, bg="lightblue")
        play.grid(row=1, column=0, sticky=tk.E, padx=20, pady=5)
        play.bind("<ButtonRelease-1>", my_controller.play_queue_popup)

        add_queue = tk.Button(self.bot_frame, text='Add to Queue', width=10, bg="lightblue")
        add_queue.grid(row=1, column=1, sticky=tk.E, padx=20, pady=5)
        add_queue.bind("<ButtonRelease-1>", my_controller.add_to_queue)

        self.song_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.song_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)




    def set_songs(self, songs):
        """ Update the listbox to display all songs """
        self.song_listbox.delete(0, tk.END)
        for song in songs:
            self.song_listbox.insert(tk.END, song)

    def selected_listbox(self):
        """ Returns the index of the selcted listbox"""
        song = self.song_listbox.index(tk.ACTIVE)
        return song

    def selected_song_info(self, song):
        """ Displays selected song information"""
        msg_str = f'Album: {song["album"]}\nGenre: {song["genre"]}\nAdded: {song["date_added"]}\n' \
                  f'Rating: {song["rating"]}/5\nRuntime: {song["runtime"]}'
        messagebox.showinfo(title='Song Info', message=msg_str)
        
    def search_keyword(self):
        """ Returns the searched keyword"""
        return self.search.get()


