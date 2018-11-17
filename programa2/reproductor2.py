from tkinter import*
from tkinter import ttk
import pygame
from pygame import mixer
import sys
from tinytag import tinytag, TinyTag


root=Tk()
root.title("reproductor")
root.geometry('300x100')
root.iconbitmap(r'C:\Users\xgian\Desktop\programa\botones\favicon.ico')
mixer.init()



#funciones
def playboton():
    mixer.music.load(fr"C:\Users\xgian\Desktop\programa\canciones\Laura Pergolizzi - Lost on You\Lost On You.mp3")
    mixer.music.play()
paused=FALSE
def pausaboton():
    mixer.music.pause()



def atrasboton():
    print("hola")
def siguienteboton():
    print("holaa")


#botones
photoatras=PhotoImage(file='atras.png')
atras=Button(root, image=photoatras, command=atrasboton)
atras.pack(side=LEFT)


photoplay=PhotoImage(file='play.png')
play=Button(root, image=photoplay, command=playboton)
play.pack(side=LEFT)


photopausa=PhotoImage(file='pausa.png')
pausa=Button(root, image=photopausa, command=pausaboton)
pausa.pack(side=LEFT)


photosiguiente=PhotoImage(file='siguiente.png')
siguiente=Button(root, image=photosiguiente, command=siguienteboton)
siguiente.pack(side=LEFT)


photoshuffle=PhotoImage(file='shuffle.png')
shuffle=Button(root, image=photoshuffle, command=siguienteboton)
shuffle.pack(side=LEFT)

photosonido=PhotoImage(file='sonido.png')
sonido=Button(root, image=photosonido, command=siguienteboton)
sonido.pack(side=LEFT)

buscador=Entry(root,width=30)
buscador.pack(side=LEFT)
buscador.pack(side=BOTTOM)


root.mainloop()

