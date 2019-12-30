from tkinter import *
import os

Main=Tk()
Main.title("SoftWork")
Main.geometry("750x600")
Main.configure(bg="white")
Main.resizable(True, True)

log=open("Log.ew", "r")
tut=log.readlines()


def unlog():
    menu=Listbox()
    
if str(tut[0][:-1])==0:
    bsop=Button(Main,
                text="Effetua il LogIn", font=("Arial", 13),
                bg="white", command=log)
    bsop.grid(row=0, column=7)
else:
    buon="Buongiorno ", str(tut[1][:-1])
    bsop=Button(Main,
                text=buon, font=("Arial", 13),
                bg="white", command=unlog)
    bsop.grid(row=0, column=7)
