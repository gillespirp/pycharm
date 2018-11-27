#IMPORTANTE, ANTES DE INICIAR EL PROGRAMA ASEGURESE DE TENER LAS IMAGENES QUE SE USARAN EN LA MISMA CARPETA DONDE SE
#ENCUENTRA EL ARCHIVO DE ESTE TRABJO EN PUTHON, TAMBIEN DE COLOCAR CORRECTAMENTE LOS NOMBRES DE LAS IMAGENES SIEMPRE DE TIPO
#PNG O GIF EN SUS RESPECTIVOS LUGARES DEL ALGORITMO, POR EJEMPLO EN playPhoto = PhotoImage(file="NOMBRE DE LA IMAGEN")
#DESCARGAR PYGAME PREVIAMENTE
#DESCARGAR TINYTAG PREVIAMENTE

import os
import tkinter.messagebox
from tkinter import *       #tkinter nos permitira abrir una venta cualquiera en la que pondremos imagenes y archivos
from tkinter import filedialog
from pygame import mixer  #ahora que tenemos la imagen nos ayudamos del pygame para reproducir sonidos con el import mixer
import sys
from tinytag import tinytag, TinyTag

ventana = Tk()                  #iniciamos la creacion de l ventana

statusbar= Label(ventana,text="Welcome to your music",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

menubar =Menu(ventana)          #creamos un menu que ira en la parte superior de la ventana
ventana.config(menu=menubar)
submenu =Menu(menubar, tearoff=0)#en ese menu irán sub menus a los cuales definirimos con File y Help

playlist=["/Users/Usuario/Downloads/cel_musica/"]             #la playlist contendra la ruta de la carpeta que cocntiene las canciones, asegurese de colocarla correctamente


def browse_file():              #con esta def encontraremos la carpeta de donde salen las canciones
    global filename_path
    filename_path=filedialog.askopenfilename()
    add_to_playlist(filename_path)



def add_to_playlist(filename):     #le añaderimos archivos a la lista que hemos creado presionando "add" para poder reproducirlos posteriormente
    filename= os.path.basename(filename)
    index=0
    playlistbox.insert(index,filename)
    playlist.insert(index,filename_path)
    index +=1

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open",command=browse_file)   #open lo que hara es crear una miniventana, si la presionams nos permitira escoger una cancion cualquiera de alguna carpeta(solo archivo MP3)
submenu.add_command(label="Exit",command=ventana.destroy)#con la funcion de command destroy , si la presionamos cerrara la ventana

def sobre_nosotros():

    tkinter.messagebox.showinfo("grupo de la cancion",'Acerca del nombre de la cancion')#Este sera el titulo y texto de la ventana si presionas "sobre nosotros"

submenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help",menu=submenu)
submenu.add_command(label="Sobre la cancion",command=sobre_nosotros)#llamamos con command a la def sobre_nosotros que abrira otra ventana



mixer.init()    #recien inicia la funcion mixer


ventana.geometry('320x420')    #aqui le damos tamaño a la ventana donde ira el boton(es) de "play"
ventana.title("Music")        #nombre de la ventana
ventana.iconbitmap('icono.ico')
text = Label(ventana, text='Reproductor de musica')   #titulo que ira en la ventana
text.pack(pady=10)

leftframe = Frame(ventana)
leftframe.pack(side=LEFT, padx=30)#Aqui vamos a agregar uns lista que posteriormente sera una lista de canciones

playlistbox=Listbox(leftframe,height=15,width=20 )
playlistbox.pack()

scrollbar = Scrollbar(ventana, orient="vertical")#Esto nos permitira acceder a una lista mas amplia solo haciendo scroll
scrollbar.config(command=playlistbox.yview)
scrollbar.pack(side="right", fill="y")
playlistbox.config(yscrollcommand=scrollbar.set)


addBtn = Button(leftframe, text="+añadir", command=browse_file)   #creamos el boton de añadir que permitira añadir canciones
addBtn.pack(side=LEFT)

rightframe = Frame(ventana)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

topframe = Frame(rightframe)
topframe.pack()

def play_music():       #con esta funcion podremos reproducir la musica que se escoga
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Musica reanudada"
        paused = FALSE
    else:
        try:
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]           #esta va a ser la cancion que se haya escogido o clickado
            mixer.music.load(play_it)                   #siempre tiene que cargar la cancion antes
            tag=tinytag.get(play_it)
            A=tag.album
            B=tag.artista
            C=tag.title
            D=tag.duration
            mixer.music.play()                          #le va a dar play a la cancion cuando presionemos el playPhoto que es basicamente el archivo papas.png
            # statusbar['text'] = "Playing music" + ' - ' + os.path.basename(filename_path)
        except:
            tkinter.messagebox.showerror('Archivo no encontrado', 'El archivo no pudo ser encontrado. Por favor intenta de nuevo. :(')       #si no se escoge el archivo correcto saldra esto


def stop_music():                       #si presionamos la imagen de detener(un cuadradito), finalizaremos la reproduccion de la cancion
    mixer.music.stop()
    statusbar['text']="Musica detenida"

paused=FALSE

def pause_music():                      #presionamos el boton de pausa para pausar la cancion
    global paused
    paused=TRUE
    mixer.music.pause()
    statusbar['text']="Pausa musica"

def rewind_music():                     #si hemos presionado el boton pausa y ahora presionamos el botn de play volvera a reproducirse la cancion
    play_music()
    statusbar['text']="Musica reanudada"

def set_vol(val):
    volume=int(val)/ 100
    mixer.music.set_volume(volume)  #los valores del volumen siempre van a ser desde el 0 hasta el 1

muted = FALSE

def mute_music():
    global muted
    if muted:       #aqui no hay mute
        mixer.music.set_volume(0.7)
        volumeboton.configure(image=volumePhoto)
        escala.set(40)
        muted= FALSE
    else:           #aqui se activa la funcion mute que pondra el volumen a 0
        mixer.music.set_volume(0)
        volumeboton.configure(image=mutePhoto)
        escala.set(0)
        muted=TRUE
middleframe= Frame(ventana)
middleframe.pack(pady=30,padx=10)   #colocamos la posicion de la ventana en pantalla al momento de iniciar el programa


playPhoto = PhotoImage(file="play.png") #seleccionamos la imagen que ira en esa ventana, solo imagenes tipo PNG y GIF
playboton = Button(ventana,image=playPhoto,command=play_music)     #volvemos a la imagen de papas.png un boton con lafuncion "Button"
playboton.pack(side=TOP,padx=10)                                                                    # con el command llamamos a la funcion previamente definida en" def play_music" en la linea 13

stopPhoto=PhotoImage(file="detener.png")
stopboton=Button(ventana,image=stopPhoto,command=stop_music)
stopboton.pack(side=TOP, padx=10)                                  #con el pad x indicamos en que posicion queremos que este la imagen

pausePhoto=PhotoImage(file='pausa.png')
pauseboton=Button(ventana, image=pausePhoto, command=pause_music)
pauseboton.pack(side=TOP)

bottomframe=Frame(ventana)
bottomframe.pack()      #a partir de aqui iran el volumen, reanudar y mute


rewindPhoto= PhotoImage(file="atras.png")
rewindboton=Button(bottomframe,image=rewindPhoto, command=rewind_music)
rewindboton.grid(row=0,column=0)

mutePhoto= PhotoImage(file='mute.png')
volumePhoto=PhotoImage(file='sonido.png')
volumeboton=Button(bottomframe,image=volumePhoto,command=mute_music)
volumeboton.grid(row=1,column=0)

escala=Scale(ventana, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
escala.set(40)  #colocamos el valor del volumen que deseamos y luego se dividirá entre 100 para que se pueuda reconocer
mixer.music.set_volume(0.4)
escala.pack(pady=20,padx=20)



def on_closing():       #si presionamos exit cerrara automaticamente el programa
    stop_music()
    ventana.destroy()


ventana.protocol("WM_DELETE_WINDOW", on_closing)


ventana.mainloop()
                        #concluimos la ventana


#Programa terminado
