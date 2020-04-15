import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os


class AudioplayerWindow(tk.Frame):
    """ Main Application Window """
    def __init__(self, parent,my_controller):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        # 1: create any instances of other support classes that are needed

        # 2: set main window attributes such as title, geometry etc
        parent.title('Audio Player')
        parent.geometry("400x400")

        # 3: set up menus if there are any
        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open')
        file_menu.add_command(label='Clear')
        file_menu.add_command(label='Quit')

        # 4: define frames and place them in the window
        top_frame = tk.Frame(master=parent)
        top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = tk.Frame(master=parent)
        mid_frame.grid(row=1, padx=30, pady=10)
        bot_frame = tk.Frame(master=parent)
        bot_frame.grid(row=2, padx=30, pady=10)

        # 5: define/create widgets, bind to events, place them in frames
        tk.Label(top_frame, text='File:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._file_value = tk.Label(top_frame, text='')
        self._file_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        tk.Label(mid_frame, text='Song Number:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._name_value = tk.Entry(mid_frame)
        self._name_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.listbox = tk.Listbox(top_frame, width=40, selectmode=tk.BROWSE)
        self.listbox.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Play', width=10, command=my_controller.do_play) \
            .grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Stop', width=10, command = my_controller.do_stop) \
                  .grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Pause', width=10, command = my_controller.do_pause) \
            .grid(row=1, column=0, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Resume', width=10, command=my_controller.do_resume) \
            .grid(row=1, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Help', width=10, command=self.display_help) \
            .grid(row=0, column=2, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='List Songs', width=10, command = my_controller.do_list) \
            .grid(row=1, column=2, sticky=tk.E, padx=20, pady=5)

    def display_help(self):
        """ Put the name in the name label """
        msg_str = 'This player can play,stop,' \
                  '\n pause and create playlists'
        messagebox.showinfo(title='Help', message=msg_str)


    def display_db_name(self, name):
        """ Put the db name in the top label """
        self._file_value['text'] = name

    def set_names(self,names):
        for name in names:
            self.listbox.insert(tk.END, name)

    @property
    def get_number(self):
        return self._name_value

    @property
    def get_listbox(self):
        return self.listbox