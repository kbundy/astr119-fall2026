import os
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

root = TkinterDnD.Tk()    # creates the root window
root.title("Image Examiner 3000")
root.config(bg="#262626")
root.minsize(400,550)

fileframe = tk.Frame(    # creates the drop zone/image render frame
     root,
     bg="#262626",
    )
buttonframe = tk.Frame(    # creates a frame for the button (for UI purposes)
     root,
     bg="#262626"
    )

zone = tk.Label(    # creates the drop zone
    fileframe,
    text="Drag files here!" ,
    fg="#e1e1e1", bg="#3E3E3E",
    width = 30, height = 11,
    font = ("Segoe UI", 15)
)
zone.pack(padx=16, pady=16,
          side=tk.LEFT
        )

button = tk.Button(    # creates a cool button
    buttonframe,
    text="Nothing to see here...",
    fg="#e1e1e1", bg="#3e3e3e",
    width=20, height=3,
    font=("Segoe UI", 15),
    borderwidth=5,
    activebackground="#3e3e3e", activeforeground="#e1e1e1",
    relief="sunken",
)
button.pack(padx=16, pady=(0, 16))

feedback = tk.Label(    # creates a feedback terminal
     root,
     text="\nNo, seriously. There's nothing here.\n",
     fg="#e1e1e1", bg="#3e3e3e",
     font=("Segoe UI", 10),
     wraplength=400,
     justify="left",
     relief="ridge"
)
feedback.pack(
     padx=16, pady=(0, 16),
     fill=tk.X, expand=True,
     side=tk.BOTTOM
    )

fileframe.pack()
buttonframe.pack()

def on_enter(event):
    zone.config(bg="#7e7e7e")    # highlights while files hover over the zone
    return event.action

def on_leave(event):
    zone.config(bg="#3e3e3e")    # reverts back to normal when files aren't hovering over the zone

def on_drop(event):
    zone.config(bg="#3e3e3e")    # reverts the zone to normal color
    
    def open_image():    # open the image file function
            file = root.tk.splitlist(event.data)    # gets the filepath as a list (?)
            filepath = file[0]    # converts file path to a string

            try:
                 img = Image.open(filepath)
                 img.show()    # opens image file
                 feedback.config(    # tells you it opened the image file
                      text=f"\nSuccessfully opened image: {filepath}\n"
                 )

            except Exception as e:    # yells at you if the file is yucky
                 feedback.config(
                      text=f"\nError loading image: {e}\n"
                 )
                 

    button.config(    # updates the button
        text="Take a gander?",
        activebackground="#848484", activeforeground="#242424",
        relief="raised",
        command=open_image
    )

    return event.action

zone.drop_target_register(DND_FILES)
zone.dnd_bind("<<DropEnter>>", on_enter)
zone.dnd_bind("<<DropLeave>>", on_leave)
zone.dnd_bind("<<Drop>>", on_drop)

root.mainloop()