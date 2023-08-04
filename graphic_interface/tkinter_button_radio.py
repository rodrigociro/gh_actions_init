import tkinter

raiz = tkinter.Tk()
raiz.title("Rodri")

def seleccionar():
    print("la opcion seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

boton1 = tkinter.Radiobutton(raiz,text="opcion 1",variable=opcion, value=1, command=seleccionar)
boton1.pack()
boton2 = tkinter.Radiobutton(raiz,text="opcion 2",variable=opcion, value=2, command=seleccionar)
boton2.pack()
boton3 = tkinter.Radiobutton(raiz,text="opcion 3",variable=opcion, value=3, command=seleccionar)
boton3.pack()

raiz.mainloop()