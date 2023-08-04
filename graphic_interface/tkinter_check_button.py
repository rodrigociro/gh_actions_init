import tkinter

raiz = tkinter.Tk()
raiz.title("Rodri")


opcion = tkinter.IntVar()
def verificar():
    valor = check1.get()
    if valor == 1:
        print("check activo")
    else:
        print("check desactivado")
    

check1 = tkinter.IntVar()

boton1 = tkinter.Checkbutton(raiz,text="si?", variable=check1, onvalue=1,offvalue=0,command=verificar)
boton1.pack()

raiz.mainloop()