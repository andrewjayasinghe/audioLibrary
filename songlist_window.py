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

        self.song_listbox = tk.Listbox(self.top_frame, width=30,
                                       selectmode=tk.BROWSE)
        self.song_scrollbar = tk.Scrollbar(self.top_frame, orient='vertical')
        self.song_scrollbar.config(command=self.song_listbox.yview)
        self.song_listbox.config(yscrollcommand=self.song_scrollbar.set)

<<<<<<< Updated upstream
        self.details = tk.Label(self.mid_frame, text='')
        self.details.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
=======
        tk.Label(self.mid_frame, text='Search:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.search = tk.Entry(self.mid_frame, width=20)
        self.search.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.details = tk.Label(self.bot_frame, text='Select and click details for more info')
        # self.details.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.details.pack()

>>>>>>> Stashed changes

        self.song_details = tk.Button(self.bot_frame, text='Details', width=10,
                                      command=my_controller.get_song_info)
        self.song_details.pack()
        
        self.edit_details = tk.Button(self.bot_frame, text='Edit Details', width=10,
                                      command=my_controller.song_details_popup)
        self.edit_details.pack()
        
<<<<<<< Updated upstream
=======
        self.search_song = tk.Button(self.bot_frame, text='Search', width=10,
                                      command=my_controller.search_song)
        self.search_song.pack()

        
>>>>>>> Stashed changes
        # self.delete_button = tk.Button(self.bot_frame, text='Delete', width=10,
        #                               command=my_controller.delete_classlist)
        # self.delete_button.pack()
        # 
        # self.close_button = tk.Button(self.bot_frame, text='Close', width=10,
        #                            command=self._close_cb)

        self.song_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.song_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # self.close_button.pack()



<<<<<<< Updated upstream
    def set_names(self, songs):
=======
    def set_songs(self, songs):
>>>>>>> Stashed changes
        """ Update the listbox to display all names """
        self.song_listbox.delete(0, tk.END)
        for song in songs:
            self.song_listbox.insert(tk.END, song)

    def selected_listbox(self):
        song = self.song_listbox.index(tk.ACTIVE)
        return song

    def selected_song_info(self, song):
        self.song_info = f'{song["artist"]} - {song["album"]} ({song["runtime"]})  {song["rating"]}/5'
        self.details['text'] = self.song_info
<<<<<<< Updated upstream
=======
        
    def search_keyword(self):
        return self.search.get()
>>>>>>> Stashed changes

    # def update_listbox(self):
    #     self.name_listbox.delete(tk.ANCHOR)

