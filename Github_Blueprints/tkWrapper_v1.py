from tkinter import *
from tkinter import ttk


class Window():
    """
    Create a Tkinter window simply by passing 3 args
    
    """
    def __init__(self,window_name='Default',WIDTH=380,HEIGHT=200):
        self.HEIGHT = str(HEIGHT)
        self.WIDTH = str(WIDTH)
        self.wn = window_name

    def main_window(self):
        root = Tk()
        root.title(self.wn)
        root.geometry(f"{self.WIDTH}x{self.HEIGHT}+200+200")
        root.resizable(False, False)
        root.configure(bg='black')
        self.root = root
        return root

    def loop(self):
        self.root.mainloop()

class WFrame():
    def __init__(self,surface):
        self.root = surface
    
    def loose_package(self,width=20,height=20,p_y=0,p_x=0,side=LEFT):
        a_frame = Frame(self.root,width=width,height=height)
        a_frame.pack(side=side,pady=p_y,padx=p_x)
        return a_frame
    def grid_package(self,width=20,height=20):
        a_frame = Frame(self.root,width=width,height=height)
        return a_frame

class WButtons():
    def __init__(self,surface):
        self.root = surface

    def loose_package(self,text='default',width=5,height=5,command=NONE,p_y=0,p_x=0,side=LEFT):
        a_button = Button(self.root, text=text,width=width, height=height, command=command)
        a_button.pack(side=side, pady=p_y,padx=p_x)
        return a_button
    
    def grid_package(self,text='default',width=5,height=5,command=NONE):
        a_button = Button(self.root, text=text,width=width, height=height, command=command)
        return a_button
    
class WCombobox():
    def __init__(self,surface):
        self.root = surface

    def loose_package(self,textvariable='Stringvar please',values ='the list please',justify='center',side=LEFT):
        a_combobox = ttk.Combobox(self.root, textvariable=textvariable,values=values)
        a_combobox.configure(justify=justify)
        a_combobox.pack(side=side)
        return a_combobox
    
    def grid_package(self,textvariable='Stringvar please',values ='the list please',justify='center'):
        a_combobox = ttk.Combobox(self.root, textvariable=textvariable,values=values)
        a_combobox.configure(justify=justify)
        return a_combobox

class Svars():
    def __init__(self,surface):
        self.root = surface

    def file_location(self):
        file_locations = StringVar(self.root)
        return file_locations
    def filename(self):
        fn = StringVar(self.root)
        return fn
    def dir_location(self):
        directory_location = StringVar(self.root)
        return directory_location 
    def audio_clist(self,index=0):
        audio_type = StringVar(self.root)
        audio_type_convertible_extensions = ["aif", "aiff", "amr", "au", "flac", "gsm", "m4a", "mp3", "ogg", "raw", "wav", "wma","mp4"]
        audio_type.set(audio_type_convertible_extensions[index])
        return audio_type,audio_type_convertible_extensions   
