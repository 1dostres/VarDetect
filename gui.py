import tkinter as tk
from tkinter import *
from tkinter import ttk
import mainhome
import video2foto
from tkinter import filedialog
import sys
from PIL import ImageTk, Image


root = tk.Tk()
root.title('TFG ANA LA INGENIERA')
root.geometry('550x400')
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Home')
tabControl.add(tab2, text='video2foto')
tabControl.pack(expand=1, fill="both")

#### Tab1 home
ttk.Label(tab1, text="Bienvenida a la aplicacion Premium para ingenieras de prestigio.").place(x = 0, y = 0)
ttk.Label(tab1, text="Esta exlcusiva aplicacion le permite convertir videos a fotos y extraer datos de esos videos.").place(x = 0, y = 20)
ttk.Label(tab1, text="Si aun no has convertido tu video a fotos, porfavor, hazlo en la ventana 'video2foto'.").place(x = 0, y = 40)
ttk.Label(tab1, text="Primero, selecciona la carpeta con las fotos: ").place(x = 0, y = 60)

###### Seleccionamos carper de fotos
fotoFolderE = Entry(tab1, width=40)
fotoFolderE.place(x = 0, y =80)

def search_path2():
    folder_selected = filedialog.askdirectory()
    fotoFolderE.delete(0, END)
    fotoFolderE.insert(0,folder_selected)

plus1 = Button(tab1, text = '+', command = search_path2).place(x = 250, y = 76)

ttk.Label(tab1, text="Ahora, selecciona el arhcivo con la foto de la bolita.").place(x = 0, y = 100)
ttk.Label(tab1, text="Es necesario que el tamaño de la imagen de la bolita se corresponda con el de la foto, para ello,").place(x = 0, y = 100)
ttk.Label(tab1, text="la mejor opcion es recortarla directamente desde donde se te abre la foto: ").place(x = 0, y = 120)

def message():
    novi = Toplevel()
    canvas = Canvas(novi, width = 500, height = 281)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'editFotoEjemplo.png')
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1

button = Button(tab1, text="i", command=message).place(x=400, y=118)

##### Seleccionamos bolita
ttk.Label(tab1, text="Selecciona el archivo de la bolita: ").place(x = 0, y = 140)
BolitapathE = Entry(tab1, width=40)
BolitapathE.place(x = 0, y =160)

def search_path3():
    folder_selected = filedialog.askopenfile()
    filepath = str(folder_selected).split("'")[1]
    BolitapathE.delete(0, END)
    BolitapathE.insert(0,filepath)

plus = Button(tab1, text = '+', command = search_path3).place(x = 250, y = 157)

## Ejecutamos y normalizamos:
ttk.Label(tab1, text="Teniendo en cuenta que la escala de la imagen es diferente a la real, necesitamos normalizar los valores.").place(x = 0, y = 180)
ttk.Label(tab1, text="Para ello, cuando pulses mostrar gráfica, primero te aparecerá una imagen que contiene la ").place(x = 0, y = 200)
ttk.Label(tab1, text="posición mas alta a la que llego la bolita, tienes que escribir en el cuadro de texto esa posicion").place(x = 0, y = 220)
ttk.Label(tab1, text="real y darle a continuar.").place(x = 0, y = 240)

def mgraf():
    fotoFolder = fotoFolderE.get()
    Bolitapath = BolitapathE.get()
    valores, maxFrame = mainhome.posBolita(fotoFolder, Bolitapath)
    
    novi2 = Toplevel()
    novi2.geometry('730x520')

    imagenL = Image.open(maxFrame)
    resize_image = imagenL.resize((700, 481))
    new_image = ImageTk.PhotoImage(resize_image)

    lblImagen = Label(novi2, image = new_image).place(x = 20,y = 40)

    ttk.Label(novi2, text="Selecciona el valor en el que se encuentra la bolita: ").place(x = 0, y = 5)
    mxBolE = Entry(novi2, width=7)
    mxBolE.place(x = 275, y =5)

    def continuar():
        mxBol = float(mxBolE.get())
        mainhome.normVal(valores, mxBol)

    plus = Button(novi2, text = 'Continuar', command = continuar).place(x = 500, y = 5)

    novi2.mainloop()



mosGraf = Button(tab1, text = 'Mostrar Grafica', command = mgraf).place(x = 0, y = 260)


ttk.Label(tab1, text="By Martin Miles").place(x = 0, y = 320)
ttk.Label(tab1, text="gonzalez.milesmartin@gmail.com").place(x = 0, y = 340)

#### Tab 2 video2foto
ttk.Label(tab2, text="Desde aqui conviertes el video en fotos, seleccionando el numero de fotos por segundo.").place(x = 0, y = 0)
ttk.Label(tab2, text="Puedes poner decimales (Si pones 0.5, te coge 1 foto cada 2 segundos)").place(x = 0, y = 20)
ttk.Label(tab2, text="Selecciona el video:").place(x = 0, y = 40)

videoPathE = Entry(tab2, width=40)
videoPathE.place(x = 0, y =60)

def search_path():
    folder_selected = filedialog.askopenfile()
    filepath = str(folder_selected).split("'")[1]
    videoPathE.delete(0, END)
    videoPathE.insert(0,filepath)

plus2 = Button(tab2, text = '+', command = search_path).place(x = 250, y = 56)


ttk.Label(tab2, text="Selecciona las fotos por segundo: ").place(x = 0, y = 80)
FpsE = Entry(tab2, width=10)
FpsE.place(x=0, y = 100)

ttk.Label(tab2, text="Selecciona la carpeta donde se van a guardar las fotos (creala antes de llegar aqui):").place(x = 0, y = 120)

fotoPathE = Entry(tab2, width=40)
fotoPathE.place(x = 0, y =140)

def search_path1():
    folder_selected = filedialog.askdirectory()
    fotoPathE.delete(0, END)
    fotoPathE.insert(0,folder_selected)

plus3 = Button(tab2, text = '+', command = search_path1).place(x = 250, y = 136)


def ejecutarVideoFoto():
    videoPath = videoPathE.get()
    FpsV = float(FpsE.get())
    fotoFolderPath = fotoPathE.get()

    video2foto.mainVideo(videoPath, FpsV, fotoFolderPath)


execu = Button(tab2, text = 'Ejecutar', command = ejecutarVideoFoto).place(x = 0, y = 180)
ttk.Label(tab2, text="Le lleva un rato, espera hasta que el boton de ejecutar este normal").place(x = 0, y = 200)

root.mainloop()