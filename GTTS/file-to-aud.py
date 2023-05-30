from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=300,height=300)
canvas.pack()
def textospeech():
    text=entry.get()
    output=gTTS(text=text,lang="en",slow=False)
    output.save("file.mp3")
    os.system("start file.mp3")

entry=Entry(root)
canvas.create_window(200,180,window=entry)
button=Button(text="Start",command=textospeech)
canvas.create_window(200,230,window=button)
root.mainloop()
