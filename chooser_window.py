import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os


class ChooserWindow(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent, my_controller):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        # 1: create any instances of other support classes that are needed
        # self.student_names = Victimizer()

        # 2: set main window attributes such as title, geometry etc
        parent.title('Chooser')
        parent.geometry("400x200")

        # 3: set up menus if there are any
        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=my_controller.openfile)
        file_menu.add_command(label='Clear', command=my_controller.clear_callback)
        file_menu.add_command(label='Quit', command=my_controller.quit_callback)

        # 4: define frames and place them in the window
        self.top_frame = tk.Frame(master=parent)
        self.top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = tk.Frame(master=parent)
        mid_frame.grid(row=1, padx=30, pady=10)
        self.bot_frame = tk.Frame(master=parent)
        self.bot_frame.grid(row=2, padx=30, pady=10)

        # 5: define/create widgets, bind to events, place them in frames
        tk.Label(self.top_frame, text='Song URL:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._song_url = tk.Entry(self.top_frame, width=30)
        self._song_url.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # tk.Label(mid_frame, text='File name:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        # self._name_value = tk.Label(mid_frame, text='')
        # self._name_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        add_button = tk.Button(self.bot_frame, text='Add', width=10)
        add_button.grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
        add_button.bind("<Button-1>", my_controller.add_callback)

        delete_button = tk.Button(self.bot_frame, text='Delete', width=10)
        delete_button.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
        delete_button.bind("<Button-1>", my_controller.delete_callback)

        songs_button = tk.Button(self.bot_frame, text='Songs', width=10)
        songs_button.grid(row=0, column=2, sticky=tk.E, padx=20, pady=5)
        songs_button.bind("<Button-1>", my_controller.songlist_popup)

        # tk.Button(self.bot_frame, text='Stop', width=10).grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)

        # tk.Button(self.bot_frame, text='Play', width=10).grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
        #
        # tk.Button(self.bot_frame, text='Help', width=10, command=self.display_help).grid(row=0, column=2, sticky=tk.E, padx=20, pady=5)
        #
        
    def get_url(self):
        return self._song_url.get()
    
    def clear_url(self):
        self._song_url.delete(0, tk.END)

    def display_help(self):
        """ Put the name in the name label """
        msg_str = 'This player can play,stop,' \
                  '\n pause and create playlists'
        messagebox.showinfo(title='Help', message=msg_str)

    def display_db_name(self, name):
        """ Put the db name in the top label """
        self._file_value['text'] = name
