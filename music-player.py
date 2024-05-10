import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer as mxr

root = Tk()
root.title("Music Player")
root.geometry("465x700+290+10")
root.configure(bg='#333333')
root.resizable(False, False)
mxr.init()

# Function to add music
def load_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist_box.insert(END, song)

# Function to play music
def play_music():
    selected_music = playlist_box.get(ACTIVE)
    print(selected_music[0:-4])
    mxr.music.load(playlist_box.get(ACTIVE))
    mxr.music.play()

# Icon
lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=350)

image_icon = PhotoImage(file="logo png.png")
root.iconphoto(False, image_icon)

frame_count = 30
frames = [PhotoImage(file='UEx9.gif', format='gif -index %i' % (i)) for i in range(frame_count)]

def update_image(ind):
    frame = frames[ind]
    ind += 1
    if ind == frame_count:
        ind = 0
    label.configure(image=frame)
    root.after(40, update_image, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update_image, 0)

# Buttons
play_button = PhotoImage(file="play1.png")
Button(root, image=play_button, bg="#FFFFFF", bd=0, height=60, width=60, command=play_music).place(x=215, y=430)

stop_button = PhotoImage(file="stop1.png")
Button(root, image=stop_button, bg="#FFFFFF", bd=0, height=60, width=60, command=mxr.music.stop).place(x=130, y=430)

volume_button = PhotoImage(file="volume.png")
Button(root, image=volume_button, bg="#FFFFFF", bd=0, height=60, width=60, command=mxr.music.unpause).place(x=50, y=430)

pause_button = PhotoImage(file="pause1.png")
Button(root, image=pause_button, bg="#FFFFFF", bd=0, height=60, width=60, command=mxr.music.pause).place(x=300, y=430)

# Labels
menu_image = PhotoImage(file="menu.png")
Label(root, image=menu_image).place(x=0, y=580, width=485, height=120)

frame_music = Frame(root, bd=0, relief=RIDGE)
frame_music.place(x=0, y=560, width=490, height=100)

Button(root, text="Search Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#FFFFFF",
       command=load_music).place(x=0, y=520)

scrollbar = Scrollbar(frame_music)
playlist_box = Listbox(frame_music, width=100, font=("Times new roman", 10), bg="#333333", fg="white",
                       selectbackground="pink", cursor="hand2", bd=0, yscrollcommand=scrollbar.set)
scrollbar.config(command=playlist_box.yview)
scrollbar.pack(side=RIGHT, fill=Y)
playlist_box.pack(side=RIGHT, fill=BOTH)

# Run Tkinter
root.mainloop()
