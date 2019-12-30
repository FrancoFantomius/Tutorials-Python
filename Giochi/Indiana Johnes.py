from tkinter import *

Main=Tk()
Main.title("Indiana Johnes")
Main.geometry("450x500")
Main.configure(bg="orange")

linea=9

def W(linea):
    linea=linea-1
    print(linea)
    return linea

Main.bind("w", W(linea))

Pl=Label(Main,
         text="P",
         bg="red")
Pl.grid(row=linea, column=0)
