from tkinter import *

def prendi(event=None):
    testo1=testo.get(0.0,END)
    testo1=testo1.split(" ")
    print(testo1)    

window=Tk()
window.title("Scrivi")
testo=Text(window, font="Arial")
testo.pack()

testo["bg"]="#ffffff"

window.bind("<Return>", prendi)


window.mainloop()
