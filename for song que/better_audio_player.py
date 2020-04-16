# from completed_library import AudioLibrary
import vlc
import os
from player_window import AudioplayerWindow
from song_que_window import ClasslistWindow
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from flask import request
import requests

class AudioPlayer(tk.Frame):
    """
    This is a better Audio Player (ie: better than the first simple player
    we used. This class consists of a number of commands to instantiate and
    control a vlc instance, as well as a command loop to accept and process
    user commands via a command line interface (cli).

    Once instantiated the player can be controlled by the following commands:
    play list state time pause resume quit stop help
    Each of these commands is implemented in a corresponding method that
    is prefixed with do_, for example do_play, do_help, etc.

    The player is very rudimentary and does not include provisions for
    queueing songs to play, or for playing playlists or podcasts.
    """

    def __init__(self, media_path):
        tk.Frame.__init__(self)
        self._root_win = tk.Toplevel()
        self._player_window = AudioplayerWindow(self._root_win, self)
        print("Starting the Audio Player ...")
        self._vlc_instance = vlc.Instance()
        self._player = self._vlc_instance.media_player_new()
        print("Initializing media library ...")
        self._library = AudioLibrary()
        self._library.load()
        self._current_title = None
        print("\nWelcome to the Audio Player.\n")

    def do_list(self):
        """ List all song titles with numbers for playback etc """
        self._player_window.get_listbox.delete(0, tk.END)
        tags = []
        for title in sorted(self._library.titles()):
            tags.append(self._library.get_song(title).meta_data())
        box = []
        for i, tag in enumerate(tags):
            box.append(f"{i+1}. {tag['title']}")
        self._player_window.set_names(box)


    def do_play(self):
        """Play a song specified by number. """
        listbox = self._player_window.get_listbox
        active = listbox.get(tk.ACTIVE)
        names = active.split('.')
        num = names[0]#self._player_window.get_number.get()
        title = self._get_title_from_num(num)
        if title is None:
            print(f"Invalid song num: {num}. Syntax is: play song_num. Use "
                  f"list to get song_num's.")
            return
        song = self._library.get_song(title)

        if self._player.get_state() == vlc.State.Playing:
            self._player.stop()
        media_file = song.get_location()
        media = self._vlc_instance.media_new_path(media_file)
        self._player.set_media(media)
        self._player.play()
        self._current_title = title
        print(f"Playing {title} from file {media_file}")

    def _get_title_from_num(self, num):
        """ Find the title of a song, given its song number (as displayed
            from list, and as entered by the user).
        """
        try:
            song_num = int(num)
            title = self._library.titles()[song_num - 1]
        except (IndexError, ValueError, TypeError):
            title = None
        return title

    def do_pause(self):
        """ Pause the player """
        if self._player.get_state() == vlc.State.Playing:
            self._player.pause()
        print(f"Player paused during playback of {self._current_title}")

    def do_resume(self):
        """ Resume playing """
        if self._player.get_state() == vlc.State.Paused:
            self._player.pause()
        print(f"Playback of {self._current_title} resumed")

    def do_stop(self):
        """ Stop the player """
        self._player.stop()
        print(f"Player stopped")

    def do_quit(self):
        """ Terminate the program """
        self._player.stop()
        self._player.release()
        print(f"Audio Player exiting.")
        exit(0)

    def do_state(self, args):
        """ Display state of the player. """
        state = str(self._player.get_state()).split('.')[1]
        print(f'Current player state is {state}')
        print(f'Current song: {self._current_title}')
        print(f'Playback posn: {self._get_current_posn()}')

    def do_time(self, args):
        """ Display current play time of current song. """
        if self._current_title is None:
            print("No song playing.")
        else:
            print(f'{self._current_title} {self._get_current_posn()}')

    def _get_current_posn(self):
        """ Return current play time (position in) current song. """
        if self._current_title is None:
            return f"No song playing."
        song = self._library.get_song(self._current_title)
        runtime = song.runtime
        remaining_secs = int(round(self._player.get_time() / 1000, 0))
        mins = int(remaining_secs // 60)
        secs = int(remaining_secs % 60)
        return f"at {mins}:{secs:02d} ... of {runtime}"

    def do_help(self, args):
        """ List names of all methods that can run as commands. """
        methods = [m for m in dir(AudioPlayer) if 'do_' in m]
        cmd_names = "  ".join(methods).replace('do_', '')
        print(f"Commands: " + cmd_names)

    def cmdloop(self):
        """ Process keyboard commands. """
        prompt = "\nEnter command (? for help): "
        while True:
            cmd = input(prompt)
            self._dispatch(cmd)

    def _dispatch(self, args):
        """ Valid commands all must have a method in this class that starts
            with prefix 'do_' (example: do_play). Run the appropriate method
            or display a warning. Accept '?' as a synonym for 'help'. Always
            pass arguments as a single arg, or None if no args specified on
            the command line.
        """
        if args == '':
            return
        if args == '?':
            args = 'help'
        arg_list = args.split()
        cmd = f'do_{arg_list[0]}'
        if not self._valid_cmd(cmd):
            print("Invalid command: ", args)
            return
        if len(arg_list) <= 1:
            args = None
        else:
            args = ' '.join(arg_list[1:])
        command = f"self.{cmd}({args})"
        eval(command)

    def que_popup(self):
        self._class_win = tk.Toplevel()
        self._class = ClasslistWindow(self._class_win)

    @staticmethod
    def _valid_cmd(cmd):
        """ Check that a function to run the command exists in this class. """
        if cmd in dir(AudioPlayer):
            return True
        else:
            return False


if __name__ == "__main__":
    media_path = os.path.join(os.getcwd(), "mp3")   # path to a dir with mp3's
    root = tk.Tk()
    AudioPlayer(media_path).pack()
    tk.mainloop()
