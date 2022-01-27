#Importing Required Modules & libraries
from tkinter import *
from tkinter.ttk import *
from pygame import mixer
import pygame
import os

DEBUG = True

class MusicPlayer:
    """One object of this class represents a tkintr GUI
application that plays
    audio files and can write and read a .m3u playlist."""
    def __init__(self, root):
        """TODO: Creates a tkinter GUI application that plays
audio files and 
        can write and read a .m3u playlist."""
        self.playlistfilename = 'playlist.m3u'
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()
        # Creating trackframe for songtrack label & tracksttus lable
        trackframe = LabelFrame(self.root, text="Song Track",
relief = GROOVE)
        trackframe.place(x=0, y=0, width = 600, height = 100)
        songtrack = Label(trackframe,
textvariable=self.track).grid(
            row = 0, column = 0, padx = 10, pady = 5
)
        trackstatus = Label(trackframe,
textvariable=self.status).grid(
            row = 0, column = 1, padx = 10, pady = 5
)
        #Creating buttonframe
        buttonframe = LabelFrame(self.root, text = "Control Panel", relief = GROOVE)
        #Inserting song control Buttons
        buttonframe.place(x = 0, y = 100, width = 600, height = 100)
        Button(buttonframe, text = "Play", command = self.playsong).grid(
            row = 0, column = 0, padx = 10, pady = 5
        )
        Button(buttonframe, text="Pause", command = self.pausesong).grid(
            row = 0, column = 1, padx = 10, pady = 5
        )
        Button(buttonframe, text="Unpause", command = self.unpausesong).grid(
            row = 0, column = 2, padx = 10, pady = 5
        )
        Button(buttonframe, text="Stop", command = self.stopsong).grid(
            row = 0, column = 3, padx = 10, pady = 5
        )
        Button(buttonframe, text = "Load Playlist", command = self.loadplaylist).grid(
            row = 1, column = 0, padx = 10, pady = 5
        )
        Button(buttonframe, text="Save Playlist", command = self.saveplaylist).grid(
            row = 1, column = 1, padx = 10, pady = 5
        )
        Button(buttonframe, text="Remove Song", command = self.removesong).grid(
            row = 1, column = 2, padx = 10, pady = 5
        )
        Button(buttonframe, text="Refresh From Folder", command = self.refresh).grid(
            row = 1, column = 3, padx = 10, pady = 5
        )
        # TODO: Insert playlist control Buttons

        # Creating songsframe
        songsframe = LabelFrame(self.root, text = "Song Playlist",
relief = GROOVE)
        songsframe.place(x = 600, y = 0, width = 400, height = 200)
        scrol_y = Scrollbar(songsframe, orient = VERTICAL)
        self.current_playlist = []
        self.playlist = Listbox(songsframe, 
                                yscrollcommand = scrol_y.set,
                                selectbackground = "gold",
                                selectmode = SINGLE,
                                relief = GROOVE)

        # Applying Scrollbar to playlist Listbox
        scrol_y.pack(side = RIGHT, fill = Y)
        scrol_y.config(command = self.playlist.yview)
        self.playlist.pack(fill = BOTH)

        # Changing directory for fetching songs
        os.chdir("./music")
        #Inserting songs into playlist
        self.refresh()
    
    def playsong(self):
        """Displays selected song and its playing status and 
plays the song"""
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):
        """Displays stopped status and stops the song."""
        self.status.set("-Stopped")
        pygame.mixer.music.pause()
    
    def pausesong(self):
        """Displays paused status and pauses the song."""
        self.status.set("-Paused")
        pygame.mixer.music.pause()
    
    def unpausesong(self):
        """Displays the playing status and unpauses the song."""
        self.status.set("-Playing")
        pygame.mixer.music.unpause()
    
    def removesong(self):
        """Deletes the active song from the playlist."""
        self.current_playlist.remove(self.playlist.get(ACTIVE))
        self.playlist.delete(ACTIVE)
    
    def loadplaylist(self):
        """TODO: Clears the current playlist and loads a previously 
saved playlist
        from the music folder. A user friendly message is
appended to the status
        if a FileNotFoundrror is caught(see the demo video).
        All other exception messages are
        appended to the status in their default string form.
        Ignore the lines that start with #.
        """
        list_filename = os.getcwd()+'/playlist.m3u'
        try:
            file = open(list_filename, 'r')
            lists = file.read()
            self.current_playlist = lists.split('\n')
            file.close()
            self.playlist.delete(0, END)
            for each_file in self.current_playlist:
                if not each_file.startswith('#'):
                    self.playlist.insert(END, each_file)
        except FileNotFoundError:
            self.status.set('file playlist.m3u was not found')
        except Exception as e:
            self.status.set(e)

    def saveplaylist(self):
        """TODO: Save the current playlist to the playlist file
in the music
        folder. All exception messages are appended to the status
in their
        default string form.
        Make sure the first line of the file is only:
        #EXTM3U
        # """
        try:
            list_filename = os.getcwd()+'/playlist.m3u'
            file = open(list_filename, 'w')
            file.write('#EXTM3U\n')
            file.write('\n'.join(self.current_playlist))
            file.close()
        except Exception as e:
            self.status.set(e)

    def refresh(self):
        """
        TODO:
        Clears the current playlist and fills it with all valid 
sound files
        from the music folder. All exception messages are 
append to the status
        in their default string form.
        Insert items into a tkinter
        Listbox.
        """
        # current_dir = os.getcwd()
        self.playlist.delete(0, END)
        try:
            for each_file in os.listdir():
                if(each_file[0] != '.' and each_file.endswith(('.ogg','.mp3','.wav'))):
                    self.current_playlist.append(each_file)
                    self.playlist.insert(END, each_file)
        except Exception as e:
            self.status.set(e)
def main():
    """Create main window and start a MusicPlayer application on it."""
    # Creating TK root window
    root = Tk()
    # Passing root to the MucisPlayer constructor
    app = MusicPlayer(root)
    # Start the main GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()