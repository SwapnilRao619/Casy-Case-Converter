import tkinter as ui
from tkinter import ttk
import tkinter.font 
import pygame
from threading import Thread

window=ui.Tk()
window.geometry("400x420")
window.title("Casy: Case Converter")

def music():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)

def stop():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        mt = Thread(target=music)
        mt.start()

pygame.mixer.init()
mt=Thread(target=music)
mt.start()

l1=ui.Label(window, text="Enter the text that has to be converted:", foreground="black", background="yellow",width=50, height=2, font=('Helvetica bold', 12))
l1.pack()

e1=ui.Entry(window, fg="white", bg="#fc03a9",width=59, font=('Helvetica bold', 26))
e1.pack(ipady=50, pady=15)
text=e1.get()

bframe=ui.Frame(window)
b1=ui.Button(bframe,text="lower case", width=14, height=2, bg="#c92292", fg="black")
b2=ui.Button(bframe,text="UPPER CASE", width=14, height=2, bg="#c92292", fg="black")
b3=ui.Button(bframe,text="Camel Case", width=14, height=2, bg="#c92292", fg="black")
b4=ui.Button(bframe,text="Sentence case", width=14, height=2, bg="#c92292", fg="black")
b5=ui.Button(bframe,text="aLtErNaTiNg CaSe", width=14, height=2, bg="#c92292", fg="black")
b6=ui.Button(bframe,text="Reset", width=14, height=2, bg="#c92292", fg="black")
b7=ui.Button(bframe,text="Copy Text", width=14, height=2, bg="#c92292", fg="black")
b8=ui.Button(bframe,text="Mute/Unmute", width=14, height=2, bg="#c92292", fg="black",command=stop)
b1.grid(row=0,column=0,padx=5,pady=5)
b2.grid(row=0,column=1,padx=5,pady=5)
b3.grid(row=1,column=0,padx=5,pady=5)
b4.grid(row=1,column=1,padx=5,pady=5)
b5.grid(row=2,column=0,padx=5,pady=5)
b6.grid(row=2,column=1,padx=5,pady=5)
b7.grid(row=3,column=0,padx=5,pady=5)
b8.grid(row=3,column=1,padx=5,pady=5)
bframe.pack()



window.mainloop()