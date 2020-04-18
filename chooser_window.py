import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os


class ChooserWindow(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent, my_controller):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)


        parent.title('Main')
        parent.geometry("330x200")


        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=my_controller.openfile)
        file_menu.add_command(label='Quit', command=my_controller.quit_callback)


        self.top_frame = tk.Frame(master=parent)
        self.top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = tk.Frame(master=parent)
        mid_frame.grid(row=1, padx=30, pady=10)
        self.bot_frame = tk.Frame(master=parent)
        self.bot_frame.grid(row=2, padx=30, pady=10)


        tk.Label(self.top_frame, text='Song URL:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._song_url = tk.Entry(self.top_frame, width=30)
        self._song_url.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        add_button = tk.Button(self.bot_frame, text='Add', width=10, bg="lightblue")
        add_button.grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
        add_button.bind("<ButtonRelease-1>", my_controller.add_callback)

        delete_button = tk.Button(self.bot_frame, text='Delete', width=10, bg="lightblue")
        delete_button.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
        delete_button.bind("<ButtonRelease-1>", my_controller.delete_callback)

        help_button = tk.Button(self.bot_frame, text='Help', width=10, bg="lightblue")
        help_button.grid(row=1, column=0, sticky=tk.E, padx=20, pady=5)
        help_button.bind("<ButtonRelease-1>", self.display_help)

        songs_button = tk.Button(self.bot_frame, text='Songs List', width=10, bg="lightgreen")
        songs_button.grid(row=1, column=1, sticky=tk.E, padx=20, pady=5)
        songs_button.bind("<ButtonRelease-1>", my_controller.songlist_popup)


    def get_url(self):
        """ Returns the filepath"""
        return self._song_url.get()
    
    def clear_url(self):
        """Clears the URL"""
        self._song_url.delete(0, tk.END)

    def display_help(self, event):
        """ Displays basic information of the player"""
        msg_str = 'Main Window:\n1) Add or Remove a song by inputing the local file URL or use file > open' \
                  '\n2) View your songs by clicking "Songs List"\n' \
                  '\nSong List Window:\n1) Leave search bar empty to get full list of songs' \
                  '\n2) Select and hit "Open Player" to start the queue' \
                  '\n3) Select and click "Add to Queue" to add songs once the player is open'
        messagebox.showinfo(title='Help', message=msg_str)

