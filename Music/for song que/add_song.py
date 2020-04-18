import tkinter as tk

class AddSongWindow(tk.Frame):

    def __init__(self,parent):
        """ Initialize the popup add student window """
        tk.Frame.__init__(self,parent)


        parent.title('Add')
        parent.geometry("400x200")


        self.top_frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)
        mid_frame = tk.Frame(self.master)
        mid_frame.grid(row=1, padx=30, pady=10)
        self.top_frame.grid(row=0, padx=30, pady=10)
        self.bot_frame.grid(row=2, padx=30, pady=10)

        tk.Label(mid_frame, text='Song number:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._student_number = tk.Entry(mid_frame, width=20)
        self._student_number.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(mid_frame, text='Song Name:').grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self._fname = tk.Entry(mid_frame, width=20)
        self._fname.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.add_button = tk.Button(mid_frame, text='Add Song', width=10)

        self.add_button.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)