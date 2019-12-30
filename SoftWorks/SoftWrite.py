#Inizzializzazione
from tkinter import *
from tkinter import filedialog
import os

tit="Untitled - SoftWrite"

M=Tk()
M.title(tit)
M.configure(bg="lightblue")
#M.geometry("962x720")
M.wm_iconbitmap("SoftWrite.ico")

salv=0

#Oggetti
BG=Frame(M, bg="grey")
T=Text(BG)
SC=Scrollbar(M, command=T.yview)
T.configure(font=("Arial", 15), height=33, relief=SUNKEN, yscrollcommand=SC.set)
BG.grid(row=0, column=0, sticky="nsew")
T.grid(row=0, column=1, sticky="nsew", padx=30)
SC.grid(row=0, column=2, sticky="nsew")
BG.grid_propagate(True)
T.grid_propagate(True)
SC.grid_propagate(True)


#Comandi
def N(*args):
    os.system("start SoftWrite.py")

def OP(*args):
    global tit
    global salv
    ap=filedialog.askopenfile(initialdir="\0", title="Open", filetypes=(("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")))
    tit=(ap.name + " - SoftWrite")
    M.title(tit)
    salv=1
    T.delete(1.0, END)
    for q in ap:
        T.insert(END, q)
        q=0
    ap.close()
def SAS(*args):
    try:
        t=T.get(1.0, END)
        F=filedialog.asksaveasfile(initialdir="\0", mode="w", defaultextension=".txt",
                                   filetypes=[("Text files", "*.txt"),
                                              ("All files", "*.*")])
        tit=(F.name + " - SoftWrite")
        M.title(tit)
        F.write(t)
        F.close()
        t=0
        global salv
        salv=1
    except Exception as e:
        None
def S(*args):
    def SAS(*args):
        try:
            t=T.get(1.0, END)
            F=filedialog.asksaveasfile(initialdir="\0", mode="w", defaultextension=".txt",
                                   filetypes=[("Text files", "*.txt"),
                                              ("All files", "*.*")])
            tit=(F.name + " - SoftWrite")
            M.title(tit)
            F.write(t)
            F.close()
            t=0
            global salv
            salv=1
        except Exception as e:
            None
    try:
        global salv
        t=T.get(1.0, END)
        if salv==0:
            SAS()
        else:
            global tit
            ti=tit.replace(" - SoftWrite", "")
            F=open(ti, "w+")
            F.write(t)
            t=0
            F.close()
    except Exception as e:
        None
def Sk(*args):
    try:
        global salv
        t=T.get(1.0, END)
        global tit
        ti=tit.replace(" - SoftWrite", "")
        F=open(ti, "w+")
        F.write(t)
        t=0
        F.close()
    except Exception as e:
        None
def Stampa(*args):
    def SAS(*args):
        try:
            t=T.get(1.0, END)
            F=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            tit=(F.name + " - SoftWrite")
            F.write(t)
            F.close()
            t=0
            global salv
            salv=1
        except Exception as e:
            None
    try:
        global salv
        t=T.get(1.0, END)
        if salv==0:
            SAS()
        else:
            global tit
            ti=tit.replace(" - SoftWrite", "")
            F=open(ti, "w+")
            F.write(t)
            F.close()
            t=0
            os.startfile(ti, "print")
    except Exception as e:
        None
def CL(*args):
    M.destroy()
def SICUREZZA():
    A=Tk()
    A.title("SoftWrite")
    def SAVE(*args):
        def SAS(*args):
            try:
                t=T.get(1.0, END)
                F=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
                tit=(F.name + " - SoftWrite")
                M.title(tit)
                F.write(t)
                F.close()
                t=0
                A.destroy()
                M.destroy()
            except Exception as e:
                None
        try:
            global salv
            t=T.get(1.0, END)
            if salv==0:
                SAS()
            else:
                global tit
                ti=tit.replace(" - SoftWrite", "")
                F=open(ti, "w+")
                F.write(t)
                F.close()
                t=0
                A.destroy()
                M.destroy()
        except Exception as e:
            None
    def CL():
        A.destroy()
        M.destroy()
    
    Label(A, text="Do you want to save before quit?", font=("Arial", 13)).grid(row=0, column=0, columnspan=2)
    Button(A, text="Yes", command=SAVE, bg="blue").grid(row=1, column=0)
    Button(A, text="No", command=CL, bg="blue").grid(row=1, column=1)
    

#Menu
me=Menu(M)
M.config(menu=me)

F=Menu(me, relief=RAISED, tearoff=0)
me.add_cascade(label="File", me=F)


#Menu - File
F.add_command(label="New", command=N, accelerator="Ctrl+N")
F.add_command(label="Open", command=OP, accelerator="Ctrl+O")
F.add_separator()
F.add_command(label="Save", command=S, accelerator="Ctrl+S")
F.add_command(label="Save as", command=SAS, accelerator="Ctrl+Shift+S")
F.add_separator()
F.add_command(label="Print", command=Stampa)
F.add_separator()
F.add_command(label="Close", command=CL, accelerator="Ctrl+W")




M.bind_all("<Control-n>", N)
M.bind_all("<Control-o>", OP)
M.bind_all("<Control-s>", S)
M.bind_all("<Control-S>", SAS)
M.bind_all("<Control-w>", CL)
M.bind_all("<Key>", Sk)


#Fine
M.protocol("WM_DELETE_WINDOW", SICUREZZA)

M.mainloop()
