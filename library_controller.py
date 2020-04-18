import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from flask import request
import requests
from player_api import AudioplayerWindow

class MainAppController(tk.Frame):
    """ Main Application Window """
    def __init__(self):
        """ Create the views """
        tk.Frame.__init__(self)
        self._root_win = tk.Toplevel()
        self._chooser = AudioplayerWindow(self._root_win, self)



if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController().pack()
    tk.mainloop()