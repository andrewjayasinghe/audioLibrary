import tkinter as tk
from tkinter import messagebox
import requests
from add_song import AddSongWindow


class ClasslistWindow(tk.Frame):

    def __init__(self, parent,my_controller):
        """ Initialize the popup listbox window """
        tk.Frame.__init__(self, parent)


        parent.title('List')
        parent.geometry("300x300")


        self.top_frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=10)
        self.bot_frame.grid(row=1, padx=30, pady=10)

        self.name_listbox = tk.Listbox(self.top_frame, width=20,
                                       selectmode=tk.BROWSE)
        self.name_scrollbar = tk.Scrollbar(self.top_frame, orient='vertical')
        self.name_scrollbar.config(command=self.name_listbox.yview)
        self.name_listbox.config(yscrollcommand=self.name_scrollbar.set)

        self.close_button = tk.Button(self.bot_frame, text='Close', width=15, command= my_controller._close_window )

        self.delete_button = tk.Button(self.bot_frame, text='Remove from Que', width=15)

        self.add_button = tk.Button(self.bot_frame, text='Add Song', width=15,
                                       command=self.add_popup)

        self.name_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.name_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.close_button.pack()
        self.delete_button.pack()
        self.add_button.pack()


    def set_names(self, names):
        """ Update the listbox to display all names """
        self.name_listbox.delete(0, tk.END)
        for name in names:
            self.name_listbox.insert(tk.END, name)


    @property
    def get_listbox(self):
        """getter for listbox"""
        return self.name_listbox


    def add_popup(self):
        """This is for opening the add student popup"""
        self._add_win = tk.Toplevel()
        self._add = AddSongWindow(self._add_win)


    def _close_window(self):
        """This is for closing the window"""
        self._add_win.destroy()


