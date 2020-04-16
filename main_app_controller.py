import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from chooser_window import ChooserWindow
from songlist_window import SonglistWindow
from song_details_window import SongDetailsWindow
import os
import requests
from song import Song
import csv
import eyed3

class MainAppController(tk.Frame):
    """ Main Application Window """
    def __init__(self, parent):
        """ Create the views """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._chooser = ChooserWindow(self._root_win, self)

    def clear_callback(self):
        """ Remove all students names from system. """
        pass

    def quit_callback(self):
        """ Exit the application. """
        self.master.quit()

    # def rand_callback(self):
    #     """ Random select a name and display on GUI. """
    #     response = requests.get("http://localhost:5000/student/random")
    #     student = Student.from_dict(response.json())
    #     if response.status_code == 200:
    #         full_name = f"{student.first_name} {student.last_name}"
    #         self._chooser.display_student_name(full_name)
    #     elif response.status_code == 404: messagebox.showinfo(
    #         title='Random', message="No names in DB")

    def openfile(self):
        """ Load all the names from the file """
        new_file = askopenfilename(filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*"))).replace('/', '\\')
        mp3_file = eyed3.load(new_file)
        seconds = int(mp3_file.info.time_secs)
        runtime = str(seconds // 60) + ":" + str(seconds % 60)
        song_data = {"title": str(getattr(mp3_file.tag, "title")),
                                "artist": str(getattr(mp3_file.tag, "artist")),
                                "runtime": runtime,
                                "album": str(getattr(mp3_file.tag, "album")),
                                "genre": str(getattr(mp3_file.tag, "genre")),
                                "file_location": new_file}

        response = requests.post("http://localhost:5000/song", json=song_data)
        if response.status_code == 200:
            msg_str = f'{str(getattr(mp3_file.tag, "title"))} added to the database'
            messagebox.showinfo(title='Open Song', message=msg_str)


    def add_callback(self, event):
        """ Save a new student name to the file. """
        URL = self._chooser.get_url()

        if URL == "" or URL[-4:] != ".mp3":
            messagebox.showerror(title='Invalid URL Entry', message='URL must be a local mp3 file')
            return

        mp3_file = eyed3.load(URL)
        seconds = int(mp3_file.info.time_secs)
        runtime = str(seconds // 60) + ":" + str(seconds % 60)
        song_data = {"title": str(getattr(mp3_file.tag, "title")),
                     "artist": str(getattr(mp3_file.tag, "artist")),
                     "runtime": runtime,
                     "album": str(getattr(mp3_file.tag, "album")),
                     "genre": str(getattr(mp3_file.tag, "genre")),
                     "file_location": URL}

        self._chooser.clear_url()

        response = requests.post("http://localhost:5000/song", json=song_data)
        if response.status_code == 200:
            # response = requests.get("http://localhost:5000/student/names")
            # name_list = [f'{s["first_name"]} {s["last_name"]}' for s in response.json()]
            # self._class.set_names(name_list)
            msg_str = f'{str(getattr(mp3_file.tag, "title"))} added to the database'
            messagebox.showinfo(title='Add Song', message=msg_str)

    def delete_callback(self, event):
        """ Remove students names from system. """
        URL = self._chooser.get_url()

        if URL == "" or URL[-4:] != ".mp3":
            messagebox.showerror(title='Invalid URL Entry', message='URL must be a local mp3 file')
            return

        mp3_file = eyed3.load(URL)

        self._chooser.clear_url()

        response = requests.delete("http://localhost:5000/song/" + URL)
        if response.status_code == 200:
            msg_str = f'{str(getattr(mp3_file.tag, "title"))} deleted from the database'
            messagebox.showinfo(title='Delete Song', message=msg_str)
            
    def update_callback(self, event):
        """ Remove students names from system. """
        song = self._song_details.updated_data()
        response = requests.put("http://localhost:5000/song/" + song["file_location"], json=song)
        self._song_details.destroy()
        if response.status_code == 200:
            msg_str = f'{song["title"]} updated to the database'
            messagebox.showinfo(title='Update Song', message=msg_str)


    def songlist_popup(self, event):
        self._song_win = tk.Toplevel()
        self._songlist = SonglistWindow(self._song_win, self)
        response = requests.get("http://localhost:5000/song/all")
        song_list = [f'{s["title"]}' for s in response.json()]
<<<<<<< Updated upstream
        self._songlist.set_names(song_list)
=======
        self._songlist.set_songs(song_list)
>>>>>>> Stashed changes

    def song_details_popup(self):
        index = self._songlist.selected_listbox()
        response = requests.get("http://localhost:5000/song/all")
        selected_song = response.json()[index]
        self._song_details_win = tk.Toplevel()
        self._song_details = SongDetailsWindow(self._song_details_win, self, selected_song)

    def get_song_info(self):
        index = self._songlist.selected_listbox()

        songs = requests.get("http://localhost:5000/song/all")

        selected_song = songs.json()[index]
        self._songlist.selected_song_info(selected_song)
<<<<<<< Updated upstream
        
        # response = requests.delete("http://localhost:5000/student/" + selected_student["student_id"])
        # 
        # if response.status_code == 200:
        #     self._class.update_listbox()
        #     msg_str = f'{selected_student["first_name"]} deleted from the database'
        #     messagebox.showinfo(title='Delete Student', message=msg_str)
=======

    def search_song(self):
        attributes = ("title", "artist", "album", "genre")
        searched_songs = []

        keyword = self._songlist.search_keyword()
        songs = requests.get("http://localhost:5000/song/all")

        if keyword != "":
            for song in songs.json():
                for attr in song:
                    if attr in attributes and keyword in song[attr]:
                        if song not in searched_songs:
                            searched_songs.append(song)
            song_list = [f'{s["title"]}' for s in searched_songs]
            self._songlist.set_songs(song_list)
        else:
            song_list = [f'{s["title"]}' for s in songs.json()]
            self._songlist.set_songs(song_list)

>>>>>>> Stashed changes

    # def classlist_popup(self, event):
    #     """ Show Classlist Popup Window """
    #     self._class_win = tk.Toplevel()
    #     self._class = ClasslistWindow(self._class_win, self._close_classlist_popup, self)
    #     response = requests.get("http://localhost:5000/student/names")
    #     name_list = [f'{s["first_name"]} {s["last_name"]}' for s in response.json()]
    #     self._class.set_names(name_list)
    #
    # def _close_classlist_popup(self):
    #     """ Close Classlist Popup """
    #     self._class_win.destroy()
    #
    # def add_student_popup(self):
    #     """ Show Classlist Popup Window """
    #     self._student_win = tk.Toplevel()
    #     self._student = AddStudentWindow(self._student_win, self)
    #
    # def close_add_student_popup(self, event):
    #     """ Close Classlist Popup """
    #     self._student_win.destroy()
    #
    # def delete_classlist(self):
    #     index = self._class.selected_listbox()
    #
    #     students = requests.get("http://localhost:5000/student/names")
    #
    #     selected_student = students.json()[index]
    #
    #     response = requests.delete("http://localhost:5000/student/" + selected_student["student_id"])
    #
    #     if response.status_code == 200:
    #         self._class.update_listbox()
    #         msg_str = f'{selected_student["first_name"]} deleted from the database'
    #         messagebox.showinfo(title='Delete Student', message=msg_str)


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()
