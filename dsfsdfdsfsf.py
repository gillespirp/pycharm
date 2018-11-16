from tinytag import TinyTag
import os
path = r'C:\Users\xgian\Desktop\programa\canciones\Laura Pergolizzi - Lost on You'
lstFiles = []
lstDir = os.walk(path)
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".mp3"):
            lstFiles.append(nombreFichero+extension)
for i in lstFiles:
    cancion=i
    print(cancion)
    for i in range(1):
        tag = TinyTag.get(fr"C:\Users\xgian\Desktop\programa\canciones\Laura Pergolizzi - Lost on You/{cancion}")
        print(tag.artist)
        print(tag.album)
        print(round(tag.duration/60,2))
        print(tag.genre)
        print(tag.title)

