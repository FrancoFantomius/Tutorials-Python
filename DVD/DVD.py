from tkinter import *

Main=Tk()
Main.title("Video | Controllo")
Main.geometry("900x800")
Main.configure(bg="white")
Main.resizable(True, True)

def Personalizza(event=None):
    pers=Tk()
    pers=

def Pubblica():#wip
    lettore=open("configure.txt", "r")
    tutto=lettore.readlines()
    nome=tutto[1][:-1]
    rich=Tk()
    rich.title(nome)
    rich.geometry("900x800")
    rich.resizable(False, False)
    

Personalizza=Button(Main,
                    text="Personalizza", font=("Arial", 13),
                    command=Personalizza)
Personalizza.grid(row=0, column=0)

Pubblica=Button(Main,
                text="Pubblica", font=("Arial",13),
                command=Pubblica)
Pubblica.grid(row=0, column=1)
