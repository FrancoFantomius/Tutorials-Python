from tkinter import *


Main=Tk()
Main.title("HxD Py")
Main.geometry("900x800")
Main.configure(bg="lightgrey")
Main.resizable(True, True)


def chiudi():
    global Main
    import tkinter.messagebox as tm
    if "yes"==tm.askquestion("HxD Py", "Do you want to close?"):
        Main.destroy()

def salva():
    None


Me=Menu(Main)
Main.config(menu=Me)

F=Menu(Me)
Me.add_cascade(label="File", me=F)


F.add_command(label="Save", command=salva)
F.add_separator()
F.add_command(label="Close", command=chiudi)


Gb=Frame(Main, bg="white")
Gb.grid(row=0, column=1, sticky="NS")


Main.mainloop()
