from tkinter import *


Main=Tk()
Main.title("Prova")
Main.geometry("900x800")
Main.configure(bg="blue")

M=Menu(Main)
Main.config(me=M)

def Chiudi():
    Main.destroy()

def Ciao():
    print("Ciao")
#menu
P=Menu(M)
M.add_cascade(me=P, label="Prova")
P.add_command(label="Chiudi", command=Chiudi)
P.add_separator()
I=Menu(M)
M.add_cascade(me=I, label="Inutile")
I.add_command(label="Dimmi ciao", command=Ciao)

def MD(event):
    I.post(event.x_root, event.y_root)   #Và così e basta.
    
def CD(event):
    M.post(event.x_root, event.y_root)

#tasti
sc=Frame(Main,
         bg="cyan")

Tuttecose=Text(sc)
Tuttecose.grid(row=0, column=0, padx=100)
Label(sc, text="boh",
      font=("Arial", 18)).grid(row=1, column=0)
Button(sc, text="Ancora più boh",
       font=("Arial", 11), command=Ciao).grid(row=1, column=1)

sc.grid(row=0, column=0)

sc.bind("<Button-3>", CD)

cB=Checkbutton(text="Salutami", command=Ciao)
cB.grid(row=3, column=1)

Main.bind("<Button-3>", MD)
