''' - Interfaz V 
 - Funcionalidades V

3. Mejorar estructura Read()
5. Insertar try-except si el ID ya es existente

A ESTUDIAR - SELECT * FROM, TRY/EXCEPT, MODIFICAR DATOS EN SQL'''

import sqlite3
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Gestor base de datos de usuarios")
root.geometry("325x350")
root.iconbitmap("C:\\Python\\Practicas\\Icon.ico")

frame = Frame(root)
frame.pack()

frame2 = Frame(root)
frame2.pack()

# --- Declaración funciones menú ---

# - Menú BBD - 

def light_connect(function):
    def int_function():
        connectVar = sqlite3.connect("C:\\Python\\Practicas\\Usuarios.db")
        cursorVar = connectVar.cursor()
    
        function(connectVar,cursorVar)

        connectVar.close()
    return int_function

def connect(): # Crea una conexión y cursor a SQL
    def createFile ():
        connectVar = sqlite3.connect("C:\\Python\\Practicas\\Usuarios.db")
        cursorVar = connectVar.cursor()
        
        cursorVar.execute('''CREATE TABLE USUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR (30),
        CONTRASEÑA VARCHAR (30),
        DIRECCIÓN VARCHAR (30),
        COMENTARIOS VARCHAR (100))''')
  
        connectVar.close()
        messagebox.showinfo("Atención","BBDD creada con éxito.")
    
    import os
    if os.path.isfile("C:\\Python\\Practicas\\Usuarios.db") is True:
        answer = messagebox.askyesno("Atención","Conexión ya existente. ¿Quieres anular la conexión y volver a establecerla?")
        if answer is True:
            os.remove(r"C:\\Python\\Practicas\\Usuarios.db")
            createFile()
        else:
            pass   
    else:
        createFile()

def exit(): # Cierra la ventana
    answer = messagebox.askokcancel("Atención","¿Desea salir de la aplicación?")
    if answer is True:
        messagebox.showinfo("Hasta la próxima!","¡Gracias por usar nuestra aplicación!")
        root.destroy()
    else:
        pass
        
# - Menú Borrar - 

def delete_fields(): # Borra todos los campos de la ventana
    fieldList = [idVariable,nameVariable,passVariable,adressVariable,]
    for var in fieldList:
        var.set("")
    textComments.delete(1.0,END)
    messagebox.showwarning("Atención","Se han borrado todos los campos")

# - Menú CRUD - 

@light_connect
def create (connection,cursor): # Crea un usuario y lo introduce en la base de datos con un índice generado automáticamente
    
    fieldList = [
        nameVariable.get(),
        passVariable.get(),
        adressVariable.get(),
        textComments.get("1.0",END)
        ]

    cursor.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?)",(
        fieldList[0],
        fieldList[1],
        fieldList[2],
        fieldList[3],)
        )

    connection.commit()

    messagebox.showinfo("!","Perfil creado con éxito!")

@light_connect
def read_all(connection,cursor): # Pasa por toda la base de datos y expone la información ordenada en ventana

    cursor.execute("SELECT * FROM USUARIOS")
    extractedData = cursor.fetchall()
    
    dataString = ""
    for i in extractedData:
        listedData = list(i)
        del listedData[2]
        listedData[0] = str(listedData[0])
        dataString += (", ".join(listedData) + "\n") 

    messagebox.showinfo("Lectura de datos","{}".format(dataString))

@light_connect
def read_user(connection,cursor): # Requiere introducir la ID de un usuario para que el resto de campos se completen

    try:
        
        cursor.execute("SELECT * FROM USUARIOS WHERE ID=" + idVariable.get())
        extractedData = cursor.fetchall()
        
        for user in extractedData:
            idVariable.set(user[0])
            nameVariable.set(user[1])
            passVariable.set(user[2])
            adressVariable.set(user[3])
            textComments.delete(1.0,END)
            textComments.insert(1.0,user[4])

    except sqlite3.OperationalError:

        messagebox.showinfo("Error", " Introduzca el número de ID del usuario que desea leer.")

    connect.commit()

@light_connect
def update(connection,cursor): # Actualiza la información de un usuario con sus datos ya en ventana  

    try:

        fieldList = [
            nameVariable.get(),
            passVariable.get(),
            adressVariable.get(),
            textComments.get("1.0",END)
            ]

        cursor.execute(
            "UPDATE USUARIOS SET NOMBRE=?,CONTRASEÑA=?,DIRECCIÓN=?,COMENTARIOS=?" + "WHERE ID=" + idVariable.get(),(fieldList))
        
        messagebox.showinfo("Error"," Usuario actualizado con éxito.")
        connect.commit()
    
    except sqlite3.OperationalError:

        messagebox.showinfo("Error", " Importe los datos del usuario que quiera modificar.")

@light_connect
def delete(connection,cursor): # Introducir el ID y boesta rrar un usuario de la base de datos

    try:  
        cursor.execute("DELETE FROM USUARIOS WHERE ID=" + idVariable.get())
        
        fieldList = [idVariable,nameVariable,passVariable,adressVariable,]
        for var in fieldList:
            var.set("")
        textComments.delete(1.0,END)
        
        messagebox.showinfo("Atención","Usuario borrado con éxito!")
        

    except sqlite3.OperationalError:
        
        messagebox.showinfo("Error", "Introduzca el número de ID del usuario que desea eliminar.")

    connect.commit() 

# --- Declaración Menu() y Submenus ---

menuVar = Menu(root)
root.config(menu=menuVar)

#-

menuBBDD = Menu(menuVar,tearoff=0)
menuVar.add_cascade(label="BBDD",menu=menuBBDD)
menuBBDD.add_command(label="Conectar",command=lambda: connect())
menuBBDD.add_command(label="Salir",command=lambda: exit())

#-

menuDelete = Menu(menuVar,tearoff=0)
menuVar.add_cascade(label="Borrar",menu=menuDelete)
menuDelete.add_command(label="Borrar campos",command=lambda:delete_fields())

#-

menuCRUD = Menu(menuVar,tearoff=0)
menuVar.add_cascade(label="CRUD",menu=menuCRUD)
menuCRUD.add_command(label="Crear",command=lambda:create())
menuCRUD.add_command(label="Leer",command=lambda:read_all())
menuCRUD.add_command(label="Leer usuario",command=lambda:read_user())
menuCRUD.add_command(label="Actualizar",command=lambda:update())
menuCRUD.add_command(label="Borrar",command=lambda:delete())

#-

menuHelp = Menu(menuVar,tearoff=0)
menuVar.add_cascade(label="Ayuda",menu=menuHelp)
menuHelp.add_command(label="Licencia")
menuHelp.add_command(label="Acerca de...")

# --- Declaración Label(), Entry() ---

labelID = Label(frame, text="ID:")
labelID.grid(row=0,column=0,pady="10",padx="20")

idVariable = StringVar()
entryID = Entry(frame,textvariable=idVariable)
entryID.grid(row=0,column=1,pady="10",padx="20")

#-

labelName = Label(frame, text="Nombre:")
labelName.grid(row=1,column=0,pady="10",padx="20")

nameVariable = StringVar()
entryName = Entry(frame,textvariable=nameVariable)
entryName.grid(row=1,column=1,pady="10",padx="20")

#-

labelPass = Label(frame,text="Contraseña:")
labelPass.grid(row=2,column=0,pady="10",padx="20")

passVariable = StringVar()
entryPass = Entry(frame,textvariable=passVariable)
entryPass.grid(row=2,column=1,pady="10",padx="20")
entryPass.config(show="*")

#-

labelAdress = Label(frame, text="Dirección:")
labelAdress.grid(row=3,column=0,pady="10",padx="20")

adressVariable = StringVar()
entryAdress = Entry(frame,textvariable=adressVariable)
entryAdress.grid(row=3,column=1,pady="10",padx="20")

#-

labelComments = Label(frame, text="Comentarios:")
labelComments.grid(row=4,column=0,pady="10",padx="20")

textComments = Text(frame,width=15,height=5,wrap=WORD)
textComments.grid(row=4,column=1,pady="10",padx="20",)


scrollbComments = Scrollbar(frame,command=textComments.yview)
scrollbComments.grid(row=4,column=2,sticky="nsew")
textComments.config(yscrollcommand=scrollbComments.set)

# --- Declaración Button() ---

buttonCreate = Button(frame2,text="Crear",command=lambda:create())
buttonCreate.grid(row=5,column=0,pady="10",padx="5")

buttonRead = Button(frame2,text="Leer",command=lambda:read_all())
buttonRead.grid(row=5,column=1,pady="10",padx="5")

buttonReadUser = Button(frame2,text="Leer usuario",command=lambda:read_user())
buttonReadUser.grid(row=5,column=2,pady="10",padx="5")

buttonUpdate = Button(frame2,text="Actualizar",command=lambda:update())
buttonUpdate.grid(row=5,column=3,pady="10",padx="5")

buttonDelete = Button(frame2,text="Borrar",command=lambda:delete())
buttonDelete.grid(row=5,column=4,pady="10",padx="5")


root.mainloop()


