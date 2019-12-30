from tkinter import *

FOLT="Arial"
GRANT=15
CoLoR="black"


Main=Tk()
Main.title("WRITER")
Main.geometry("950x800")
Main.configure(bg="#1c90fd")
Main.resizable(True, True)

def file(event=None):
    Fil=Tk()
    Fil.title("")
    Fil.configure(bg="lightgrey")
    SaFe=Button(Fil,
                text="SAVE", font=(FOLT, GRANT),
                bg="white", fg="black", command=SALVA)
    SaFe.grid(row=0, column=0)

def font(FOLT):
    None

def SALVA():
    Tutto=Test.get
    safe=open("Salva.ew", "w")
    safe.write(str(Tutto))
    safe.close()


F=Button(Main,
         text="File", font=("Arial", 14),
         command=file)
F.grid(row=0, column=0, sticky="WE")

scorrimento=Scrollbar(Main)
scorrimento.grid(row=1, column=2)

Test=Text(Main,
          font=(FOLT, GRANT),
          fg=CoLoR, yscrollcommand=scorrimento.set)
Test.grid(row=1, column=1)

