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
        parent.geometry("415x400")

        # 3: set up menus if there are any
        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='Menu', menu=file_menu)
        file_menu.add_command(label='Quit', command = my_controller.do_quit)

        # 4: define frames and place them in the window
        top_frame = tk.Frame(master=parent)
        top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = tk.Frame(master=parent)
        mid_frame.grid(row=1, padx=30, pady=10)
        bot_frame = tk.Frame(master=parent)
        bot_frame.grid(row=2, padx=30, pady=10)

        # 5: define/create widgets, bind to events, place them in frames
        tk.Label(top_frame, text='Songs:', font = 'Helvetica 10 bold').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._file_value = tk.Label(top_frame, text='')
        self._file_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)


        self.listbox = tk.Listbox(top_frame, width=40, selectmode=tk.BROWSE)
        self.listbox.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Play', width=10, command=my_controller.do_play, bg = 'lightblue', font = 'Helvetica 10 bold') \
            .grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Stop', width=10, command = my_controller.do_stop, bg = 'red', font = 'Helvetica 10 bold') \
                  .grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Pause', width=10, command = my_controller.do_pause, bg = 'lightyellow', font = 'Helvetica 10 bold') \
            .grid(row=1, column=0, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Resume', width=10, command=my_controller.do_resume, bg = 'lightblue', font = 'Helvetica 10 bold') \
            .grid(row=1, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Help', width=10, command=self.display_help, bg = 'yellow', font = 'Helvetica 10 bold') \
            .grid(row=0, column=2, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='List Songs', width=10, command = my_controller.do_list, bg = 'lightgreen', font = 'Helvetica 10 bold') \
            .grid(row=1, column=2, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_frame, text='Song Que', width=10, command=my_controller.que_popup, bg = 'lightgreen', font = 'Helvetica 10 bold') \
            .grid(row=2, column=0, sticky=tk.E, padx=20, pady=5)

        self._lable = tk.Label(mid_frame, text="No song selected yet", fg = 'green', font = 'Helvetica 10 bold')
        self._lable.grid(row=0,column = 0)


    def display_help(self):
        """ Put the name in the name label """
        msg_str = 'Click list songs then select and ' \
                  '\n hit the play button'
        messagebox.showinfo(title='Help', message=msg_str)


    def display_db_name(self, name):
        """ Put the db name in the top label """
        self._file_value['text'] = name

    def set_names(self,names):
        for name in names:
            self.listbox.insert(tk.END, name)

    @property
    def get_listbox(self):
        """Getter for listbox"""
        return self.listbox

    @property
    def get_lable(self):
        """Getter for listbox"""
        return self._lable