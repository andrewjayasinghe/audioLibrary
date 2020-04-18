import tkinter as tk


class SongDetailsWindow(tk.Frame):
    def __init__(self, parent, my_controller, song):
        """ Initialize the popup song details window """
        tk.Frame.__init__(self, parent)
        self.song = song

        parent.title('Song Details')

        self.top_frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=10)
        self.bot_frame.grid(row=1, padx=30, pady=10)

        tk.Label(self.top_frame, text='Album:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.album = tk.Entry(self.top_frame, width=20)
        self.album.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(self.top_frame, text='Genre:').grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.genre = tk.Entry(self.top_frame, width=20)
        self.genre.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(self.top_frame, text='Rating:').grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        self.rating = tk.Entry(self.top_frame, width=20)
        self.rating.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        self.album.insert(0, song["album"])
        self.genre.insert(0, song["genre"])
        self.rating.insert(0, song["rating"])

        save_button = tk.Button(self.bot_frame, text='Save', width=10)
        save_button.grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
        save_button.bind("<Button-1>", my_controller.update_callback)

        
    def updated_data(self):
        """ Returns the updated details of the selected song"""
        self.song["album"]=self.album.get()
        self.song["genre"]=self.genre.get()
        self.song["rating"]=self.rating.get()
        return self.song
