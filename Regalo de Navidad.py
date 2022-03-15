from tkinter import *
from tkinter import font
from typing import Counter 
from PIL import ImageTk, Image
from tkinter.font import Font
root = Tk()
root.geometry("400x700")
root.title("Regalo de Navidad")

root.iconbitmap('SantaClaus.ico')

TitleFont = Font(
    family='Cooper Black',
    size='20'
)

SecondFont = Font(
    family='Cooper Black',
    size='18',
    weight='bold',
    slant='italic',
    underline=1
)

def Comparar():
    global backg
    global opcional

    valor = int(entry_dinero.get())
    detail = 'Detalles'
    if valor>=5000:
        paquete = "A"
        opcional = "Televisor y modular"
        zapatos = "3 pares"
        camisas = "5"
        pantalones = "5"
        backg = ImageTk.PhotoImage(Image.open('Images/RegaloA.png'))
        
    elif valor>= 2000:
        paquete = "B"
        opcional = "Una grabadora"
        zapatos = "3 pares"
        camisas = "5"
        pantalones = "5"
        backg = ImageTk.PhotoImage(Image.open("Images/RegaloB.png"))
    elif valor>= 1000: 
        paquete = "C"
        zapatos = "2 pares"
        camisas = "3"
        pantalones = "3"
        backg = ImageTk.PhotoImage(Image.open("Images/RegaloC.png"))
        opcional = ""
    else: 
        paquete = "D"
        zapatos = "1 par"
        camisas = "2"
        pantalones = "2"
        backg = ImageTk.PhotoImage(Image.open("Images/RegaloD.png"))
        opcional = ""

    LabelPaquete.configure(text=f'Paquete: {paquete}')
    LabelDetalle.configure(text=' ● Detalles')
    LabelZapatos.configure(text=f' ✔ Zapatos: {zapatos}')
    LabelCamisas.configure(text=f' ✔ Camisas: {camisas}')
    LabelPantalon.configure(text=f' ✔ Pantalones: {pantalones}')
    if opcional != "":
        LabelOpcional.configure(text=f' ✔ {opcional}')
    else:
        LabelOpcional.configure(text="")
    LabelImagen.configure(image=backg)
    entry_dinero.delete(0, END)
    

def Destroy():
    root.destroy()


title = Label(root, text="Bienvenidos a los", bg="Black", fg="#e7d10d", font=TitleFont).pack(pady=5, padx=10, ipadx=10, ipady=5)
secondtitle = Label(root, text='Regalos de Navidad', font=SecondFont, fg='#F92545').pack(pady=5, padx=10, ipadx=10)
mainimage = ImageTk.PhotoImage(Image.open('Images/SantaClaus.png'))
Labelmainimage = Label(root, image=mainimage)
Labelmainimage.place(x=10, y=115)

flagimage = ImageTk.PhotoImage(Image.open('Images/Arbol.png'))
Labelflagimage = Label(root, image=flagimage)
Labelflagimage.place(x=185, y=115)

dinero = Label(root, text="Cantidad de dinero a recibir: ").place(x=120, y=330)
entry_dinero = Entry(root, width=15, bg="grey", fg="white")
entry_dinero.place(x=150, y=360)

Button(root, text="Ingresar", bg="Black", fg="White", command=Comparar).place(x=170, y=390)
Button(root, text="Cerrar", bg="Black", fg="White", command=Destroy).place(x=175, y=425)

LabelPaquete = Label(root, text='')
LabelPaquete.place(x=165, y=470)
LabelDetalle = Label(root, text='')
LabelDetalle.place(x=220, y=500)
LabelZapatos = Label(root, text='')
LabelZapatos.place(x=240, y=530)
LabelCamisas = Label(root, text='')
LabelCamisas.place(x=240, y=560)
LabelPantalon = Label(root, text='')
LabelPantalon.place(x=240, y=590)
LabelOpcional = Label(root, text='')
LabelOpcional.place(x=240, y=620)
LabelImagen = Label(root, image='')
LabelImagen.place(x=10, y=490)

root.mainloop()