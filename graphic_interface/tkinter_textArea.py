import tkinter

raiz = tkinter.Tk()
raiz.title("Rodri")

texto = tkinter.Text(raiz)
texto.config(width=20,height=10,font=("Verdana",15),padx=10, pady=10,fg="green",selectbackground="lightgrey")
texto.pack()

raiz.mainloop()