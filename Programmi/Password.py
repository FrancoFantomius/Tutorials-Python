from tkinter import *

coll=0

Main=Tk()
Main.title("SoftWork")
Main.geometry("436x450")
Main.configure(bg="white")
Main.resizable(False, False)


def INVIO():
    safe=open("Mem.psw","r")
    nom=safe.readlines()
    prima=0
    Nom=PN.get()
    Pa1=PE.get()
    Pa2=PSE.get()
    numero=0
    if Nom=="":
        s7=Label(Main,
                 text="        Inserire l'UserName        ", font=("Arial", 15),
                 bg="white", fg="red")
        s7.grid(row=14, column=0)
        prima=1
    if Pa1=="" or Pa2=="" and prima!=1:
        s7=Label(Main,
                 text="        Inserire la PassWord        ", font=("Arial", 15),
                 bg="white", fg="red")
        s7.grid(row=14, column=0)
        prima=1
    
    if Pa1!=Pa2 and prima==0:
        s7=Label(Main,
                 text="Le due Password non coincidono", font=("Arial", 15),
                 bg="white", fg="red")
        s7.grid(row=14, column=0)
        prima=1
    if prima==0:
        for lettera in Pa1:
            numero=numero+1
        if numero<=6:
            s7=Label(Main,
                     text="   Aumenta il numero di lettere   ", font=("Arial", 15),
                     bg="white", fg="red")
            s7.grid(row=14, column=0)
        if numero>6:
            safe=open("Mem.reg", "a")
            safe.write(Pa1)
            safe.write("\n")
            safe.close()



I=Label(Main,
        text="Benvenuto nella creazione account di SoftWork",
        font=("Arial", 15),
        bg="white", fg="lime")
I.grid(row=0, column=0)

PIN=Label(Main,
          text="Inserire UserName", font=("Arial", 15),
          bg="white", fg="black")
PIN.grid(row=1, column=0)

PN=Entry(Main)
PN.grid(row=2, column=0)

PI=Label(Main,
        text="Immetti la tua PassWord", font=("Arial", 15),
        bg="white", fg="black")
PI.grid(row=3, column=0)

PE=Entry(Main)
PE.grid(row=4, column=0)

PS=Label(Main,
         text="Ripeti la tua PassWord", font=("Arial", 15),
         bg="white", fg="black")
PS.grid(row=5, column=0)

PSE=Entry(Main)
PSE.grid(row=6, column=0)

Conf=Button(Main,
            text="Crea la PassWord", font=("Arial", 15),
            bg="blue", fg="lightblue", command=INVIO(coll))
Conf.grid(row=7, column=0)


s1=Label(Main, bg="white")
s1.grid(row=8, column=0)
s2=Label(Main, bg="white")
s2.grid(row=9, column=0)
s3=Checkbutton(Main, bg="white")
s3.grid(row=10, column=0)
s4=Label(Main, bg="white")
s4.grid(row=11, column=0)
s5=Label(Main, bg="white")
s5.grid(row=12, column=0)
s6=Label(Main, bg="white")
s6.grid(row=13, column=0)

DC=Label(Main,
         text="Powered by Python and Tkinter",
         bg="white")
DC.grid(row=15, column=0)
DC1=Label(Main,
         text="Programmed by SoftWork",
         bg="white")
DC1.grid(row=16, column=0)
