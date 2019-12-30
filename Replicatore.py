from tkinter import *


Main=Tk()
Main.title("Replicatore")
Main.geometry("600x500")
Main.configure(bg="grey")
Main.resizable(True, True)

def inv(flett):
    un=uno.get()
    du=tre.get()
    mass=lim.get()
    mass=eval(str(mass))


Inizio=Label(Main,
             text="Inserisci il testo da duplicare",
             font=("Arial",15), fg="red", bg="grey")
Inizio.grid(row=0, column=1, sticky="WE")
uno=Entry(Main,
          font=("Arial", 14), bg="white")
uno.grid(row=1, column=0, sticky="WE")
due=Label(Main,
          text="parte da replicare", font=("Arial", 14),
          bg="white", fg="blue")
due.grid(row=1, column=1, sticky="WE")
tre=Entry(Main,
          font=("Arial", 14), bg="white")
tre.grid(row=1, column=2, sticky="WE")

lim=Entry(Main)
lim.grid(row=2, column=1, sticky="WE")


B1=Button(Main,
          text="Lettere",
          font=("Arial", 13), command=inv(1))
B1.grid(row=3, column=2, sticky="WE")
