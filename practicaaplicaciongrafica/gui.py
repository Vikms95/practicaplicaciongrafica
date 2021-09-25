from tkinter import *

raiz = Tk()
raiz.title("Formulario")
raiz.geometry("1650x1050")

frame = Frame(raiz,width=700,height=450)
frame.pack(fill="both")

label = Label(frame,text="Nombre",font="Arial",fg="green")
label.grid(row=0,column=0,sticky="w")
campoRellenable = Entry(frame)
campoRellenable.grid(row=0,column=1,sticky="w",padx=20)

label2 = Label(frame,text="Apellido",font="Arial",fg="green")
label2.grid(row=1,column=0,sticky="w")
campoRellenable2 = Entry(frame)
campoRellenable2.grid(row=1,column=1,sticky="w",padx=20)

label3= Label(frame, text="Contraseña",font="Arial",fg="green")
label3.grid(row=2,column=0,sticky="w")
campoRellenable3 = Entry(frame)
campoRellenable3.grid(row=2,column=1,padx=20)
campoRellenable3.config(show="*")

textLabel = Label(frame, text= "Descripción",font="Arial",fg="green")
textLabel.grid(row=3,column=0)
textComentario = Text(frame,width=16,height=5)
textComentario.grid(row=3,column=1,padx=10,pady=30)
scrollbar = Scrollbar(frame,command=textComentario.yview)
scrollbar.grid(row=3,column=2,sticky="nsew")
textComentario.config(yscrollcommand=scrollbar.set)

def popupSaludo():
    raiz = Tk()
    raiz.title("Bienvenido!")
    raiz.geometry("200x150")

    label = Label(raiz,text="Gracias por clickar!!!").pack()
    return

boton = Button(raiz,text="Pulsa aquí",command=popupSaludo)
boton.pack()








raiz.mainloop()