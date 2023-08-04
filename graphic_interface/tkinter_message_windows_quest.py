import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Rodri")

def preguntar():
    resultado = tkinter.messagebox.askquestion("titulo","quieres borrar este fichero")
    if(resultado == "yes"):
        print ("si, quiero borrar el fichero")
    else:
        print("no quiero borrar el fichero")

    boton = tkinter.Button(raiz, text="Pulsar para aviso",command=preguntar)
    boton.pack()

#crear pop up
boton = tkinter.Button(raiz, text="Pulsar para aviso",command=preguntar)
boton.pack()

raiz.mainloop()