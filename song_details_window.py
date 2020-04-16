import tkinter as tk


class SongDetailsWindow(tk.Frame):
    def __init__(self, parent, my_controller, song):
        """ Initialize the popup add student window """
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
        self.song["album"]=self.album.get()
        self.song["genre"]=self.genre.get()
        self.song["rating"]=self.rating.get()
        return self.song


    #     tk.Label(self.top_frame, text='Artist').grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
    #     self.first_name = tk.Entry(self.top_frame, width=20)
    #     self.first_name.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    # 
    #     tk.Label(self.top_frame, text='Last Name:').grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
    #     self.last_name = tk.Entry(self.top_frame, width=20)
    #     self.last_name.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    # 
    #     save_button = tk.Button(self.bot_frame, text='Save', width=10)
    #     save_button.grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
    #     save_button.bind("<Button-1>", my_controller.add_callback)
    # 
    #     close_button = tk.Button(self.bot_frame, text='Close', width=10)
    #     close_button.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
    #     close_button.bind("<Button-1>", my_controller.close_add_student_popup)
    # 
    # def get_student_data(self):
    #     """ Return a dictionary of form field values for this form """
    #     return {"student_id": self.student_id.get(), "first_name": self.first_name.get(), "last_name": self.last_name.get()}
    # 
    # def clear_form_fields(self):
    #     """ Clear the name entry box """
    #     self.student_id.delete(0, tk.END)
    #     self.first_name.delete(0, tk.END)
    #     self.last_name.delete(0, tk.END)
