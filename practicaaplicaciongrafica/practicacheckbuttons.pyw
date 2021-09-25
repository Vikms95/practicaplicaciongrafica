from tkinter import *

root = Tk()
root.title("Encuesta videojuegos")
root.geometry("300x300")

nintendo = IntVar()
sony = IntVar()
microsoft = IntVar()

def selectedOption():    
    finalOption = ""
    if (nintendo.get() == 1):
        finalOption += "Nintendo"
    if (sony.get() == 1):
        finalOption += "Sony"
    if (microsoft.get() == 1):
        finalOption += "Microsoft"

button1 = Checkbutton(root,text="Nintendo",variable=nintendo,onvalue=1,offvalue=0,command=selectedOption).pack()
button2 = Checkbutton(root,text="Sony",variable=sony,onvalue=1,offvalue=0,command=selectedOption).pack()
button3 = Checkbutton(root,text="Microsoft",variable=microsoft,onvalue=1,offvalue=0,command=selectedOption).pack()

finalMessage = Label(root)
finalMessage.pack()

root.mainloop()