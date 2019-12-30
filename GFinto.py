import tkinter as tk
import random as rd

Main=tk.Tk()
Main.title("Decidi")
Main.geometry("1080x620")
Main.configure(bg="orange")

def chiudi(close):
    return(1)

mem=open("mem.txt","r")
lel=mem.readlines()
mem.close

close=0

lel=lel.split("\n")

chiudi=tk.Button(Main,
                 text="X", font=("Arial", 15),
                 bg="red", fg="blue", command=chiudi(close))

chiudi.grid(row=0, column=0)

def al(cl):
    for ri in range(0, len(lel), 2):
        cl=cl.append(ri)
    rd.choice(cl)
    return(c1)
