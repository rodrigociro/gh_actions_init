import tkinter

raiz = tkinter.Tk()
raiz.title("Rodri")

def accion():
    if(True):
        boton1 = tkinter.Button(raiz, text="Ejecutar", command=accion)
        boton1.config(activebackground="green",)
        boton1.pack()

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(activebackground="green",)
boton.pack()

raiz.mainloop()