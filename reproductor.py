import pygame, sys
from pygame.locals import *
from pygame import mixer
import os
from tinytag import tinytag, TinyTag
#https://github.com/devsnd/tinytag
path = r'C:\Users\xgian\Desktop\programa\canciones\Laura Pergolizzi - Lost on You'
lstFiles = []
lstDir = os.walk(path)
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".mp3"):
            lstFiles.append(nombreFichero+extension)
#for i in lstFiles:
#    cancion=i
#    print(cancion)
cancion=lstFiles[0]
print(cancion)
tag = TinyTag.get(fr"C:\Users\xgian\Desktop\programa\canciones\Laura Pergolizzi - Lost on You/{cancion}")
print(tag.artist)
print(tag.album)
print(tag.duration)
print(tag.genre)
print(tag.title)
pygame.init()
mixer.init()
mixer.music.load(fr"C:\Users\xgian\Desktop\programa\canciones\Laura Pergolizzi - Lost on You/{cancion}")
mixer.music.play()
DISPLAYSURF = pygame.display.set_mode((600, 300))
pygame.display.set_caption('reproductor')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
