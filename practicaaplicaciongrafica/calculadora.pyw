from tkinter import *
import time

#hacer que el 0 a la izquierda no se muestre como carácter
#puntuacion para mil millones..
#mejorar GUI
#dejar usar solo una coma por string


#declaración raiz----------------------

root = Tk()
root.title("Calculadora de Víctor")
root.geometry("360x450")

frame = Frame()
frame.pack(fill="both",expand=True)
frame.config(bd=20,bg="blue",relief="flat",cursor="dotbox")

#pantalla1-------------------------------

screenNumber = StringVar()

calcScreen = Entry(frame, textvariable=screenNumber)
calcScreen.grid(row=1,column=0,columnspan="4",padx=10,pady=10)
calcScreen.config(bg="black",fg="green",font=5,justify="right")

#pantalla2--------------------------------

screenNumber2 = StringVar()

calcScreen2 = Entry(frame, textvariable=screenNumber2,width=45)
calcScreen2.grid(row=0,column=0,columnspan="4",padx=3,pady=3)
calcScreen2.config(bg="black",fg="green",justify="right")

#funciones-----------------------------
def display(e):
    global i
    displayb.insert(i,e)
    i += 1

def write_number(num):
    screenNumber.set(screenNumber.get() + num)

def write_operation(sign):
    screenNumber2.set(screenNumber2.get() + screenNumber.get() + sign)
    screenNumber.set("")

def complete_operation():
    screenNumber2.set(screenNumber2.get() + screenNumber.get())
    finalString = screenNumber2.get()
    screenNumber.set(eval(finalString))

def delete_operation():
    screenNumber.set(screenNumber.get()[0:-1])

def clear_operation():
    screenNumber2.set("")
    screenNumber.set("")
    
#linea 1--------------------------------

button9 = Button(frame,text="9",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("9"))
button9.grid(row=2,column=0,padx=2,pady=1)

button8 = Button(frame,text="8",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("8"))
button8.grid(row=2,column=1,padx=2,pady=1)

button7 = Button(frame,text="7",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("7"))
button7.grid(row=2,column=2,padx=2,pady=1)

buttonDiv = Button(frame,text="/",relief="solid",font="bold",width=6,height=2,command=lambda:write_operation("/"))
buttonDiv.grid(row=2,column=3,padx=2,pady=1)

#linea 2----------------------------------

button6 = Button(frame,text="6",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("6"))
button6.grid(row=3,column=0)

button5 = Button(frame,text="5",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("5"))
button5.grid(row=3,column=1)

button4 = Button(frame,text="4",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("4"))
button4.grid(row=3,column=2)

buttonMult = Button(frame,text="*",relief="solid",font="bold",width=6,height=2,command=lambda:write_operation("*"))
buttonMult.grid(row=3,column=3)

#linea 3-----------------------------------

button3 = Button(frame,text="3",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("3"))
button3.grid(row=4,column=0)

button2 = Button(frame,text="2",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("2"))
button2.grid(row=4,column=1)

button1 = Button(frame,text="1",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("1"))
button1.grid(row=4,column=2)

buttonSubs = Button(frame,text="-",relief="solid",font="bold",width=6,height=2,command=lambda:write_operation("-"))
buttonSubs.grid(row=4,column=3)

#linea 4-----------------------------------

button0 = Button(frame,text="0",relief="solid",font="bold",width=6,height=2,command= lambda:write_number("0"))
button0.grid(row=5,column=0)

buttonComma = Button(frame,text=".",relief="solid",font="bold",width=6,height=2,command=lambda:write_number("."))
buttonComma.grid(row=5,column=1)

buttonDel = Button(frame,text="<",relief="solid",font="bold",width=6,height=2,command=lambda:delete_operation())
buttonDel.grid(row=5,column=2)

buttonSum = Button(frame,text="+",relief="solid",font="bold",width=6,height=2,command=lambda:write_operation("+"))
buttonSum.grid(row=5,column=3)

#linea 5-----------------------------------

buttonOpenParent = Button(frame,text="(",relief="solid",font="bold",width=6,height=2,command=lambda:write_number("("))
buttonOpenParent.grid(row=6,column=0)

buttonCloseParent = Button(frame,text=")",relief="solid",font="bold",width=6,height=2,command=lambda:write_number(")"))
buttonCloseParent.grid(row=6,column=1)

buttonClear = Button(frame,text="C",relief="solid",font="bold",width=6,height=2,command=lambda:clear_operation())
buttonClear.grid(row=6,column=2)

buttonEquals = Button(frame,text="=",relief="solid",font="bold",width=6,height=2,command=lambda:complete_operation())
buttonEquals.grid(row=6,column=3)

#linea6----------------------------------

waterMarc = Label(frame,text="© Todos los derechos reservados Kappa")
waterMarc.grid(row=7,column=0,columnspan=9,pady=5)


#bucle tkinter----------------------------

root.mainloop()