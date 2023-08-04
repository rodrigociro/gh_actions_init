import tkinter
from tkinter import messagebox
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Rodri")

def abrir():
    ruta=filedialog.askopenfilename()
    print(ruta)
boton = tkinter.Button(raiz,text="fichero?",command=abrir)
boton.pack()

raiz.mainloop()