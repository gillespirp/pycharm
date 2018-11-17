from tkinter import*
from tkinter import ttk
root=Tk()
root.title("reproductor")
root.geometry('300x100')
root.iconbitmap(r'C:\Users\xgian\Desktop\programa\botones\favicon.ico')

#funciones
def play_btn():
    print("hola")


#botones
photoatras=PhotoImage(file='atras.png')
atras=Button(root, image=photoatras, command=play_btn)
atras.pack(side=LEFT)

photoplay=PhotoImage(file='play.png')
play=Button(root, image=photoplay, command=play_btn)
play.pack(side=LEFT)

photopausa=PhotoImage(file='pausa.png')
pausa=Button(root, image=photopausa, command=play_btn)
pausa.pack(side=LEFT)

photosiguiente=PhotoImage(file='siguiente.png')
siguiente=Button(root, image=photosiguiente, command=play_btn)
siguiente.pack(side=LEFT)

photoshuffle=PhotoImage(file='shuffle.png')
shuffle=Button(root, image=photoshuffle, command=play_btn)
shuffle.pack(side=LEFT)

photosonido=PhotoImage(file='sonido.png')
sonido=Button(root, image=photosonido, command=play_btn)
sonido.pack(side=LEFT)



root.mainloop()

