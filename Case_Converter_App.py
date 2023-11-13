import tkinter as ui
from tkinter import ttk
import tkinter.font 
import pygame
from tkinter import Tk
from threading import Thread

global count
count=0

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

e1=ui.Entry(window, fg="white", bg="#fc03a9",width=59, font=('Helvetica bold', 26))
e1.pack(ipady=50, pady=20)
e1.insert(0,'Enter the text here...')

def lowercase():
    text=e1.get()
    ntext=text.lower()
    e1.delete(0,ui.END)
    e1.insert(0,ntext)

def uppercase():
    text=e1.get()
    ntext=text.upper()
    e1.delete(0,ui.END)
    e1.insert(0,ntext)

def titlecase():
    text=e1.get()
    ntext=text.title()
    e1.delete(0,ui.END)
    e1.insert(0,ntext)
    
def sentencecase():
    text=e1.get()
    ntext=text.capitalize()
    e1.delete(0,ui.END)
    e1.insert(0,ntext)

def alternatingcase():
    text=e1.get()

def reset():
    global count
    e1.delete(0,ui.END)
    count+=1

def copytext():
    global count
    if count==0:
        pass
    else:
        text=e1.get()
        r=Tk()
        r.clipboard_append(text)
        r.update()
        r.destroy()

bframe=ui.Frame(window)
b1=ui.Button(bframe,text="lower case", width=14, height=2, bg="#c92292", fg="black",command=lowercase)
b2=ui.Button(bframe,text="UPPER CASE", width=14, height=2, bg="#c92292", fg="black",command=uppercase)
b3=ui.Button(bframe,text="Title Case", width=14, height=2, bg="#c92292", fg="black",command=titlecase)
b4=ui.Button(bframe,text="Sentence case", width=14, height=2, bg="#c92292", fg="black",command=sentencecase)
b5=ui.Button(bframe,text="aLtErNaTiNg CaSe", width=14, height=2, bg="#c92292", fg="black",command=alternatingcase)
b6=ui.Button(bframe,text="Reset", width=14, height=2, bg="#c92292", fg="black",command=reset)
b7=ui.Button(bframe,text="Copy Text", width=14, height=2, bg="#c92292", fg="black",command=copytext)
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