import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Rodri")

def avisar():
    tkinter.messagebox.showinfo("titulo","mensaje con la info")
    boton = tkinter.Button(raiz, text="Pulsar para aviso",command=avisar)
    boton.pack()

#crear pop up
boton = tkinter.Button(raiz, text="Pulsar para aviso",command=avisar)
boton.pack()

raiz.mainloop()