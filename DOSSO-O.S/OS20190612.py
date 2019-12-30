from tkinter import *
import wikipedia
fplus=0

ad1=0
ad2=0
ad3=ad1

wikipedia.set_lang("it")


ris1=0
fclose=0
flog=0

def close(event=None):
    fclose=1

def calcolatore(event=None):
    calc=Tk()
    calc.title("Calcolatore")
    calc.geometry("350x500")
    calc.configure(background="white")
    calc.resizable(True, True)
    def Add1(event=None):
        if fplus==0:
            ad1=(ad1*10)+1
            print(ad1)
        else:
            ad2=(ad2*10)+1
    def Add2(event=None):
        if fplus==0:
            ad1=(ad3*10)+2
            ad3=ad1
        else:
            ad2=(ad2*10)+2
    def Add3(event=None):
        if fplus==0:
            ad1=(ad3*10)+3
            ad3=ad1
        else:
            ad2=(ad2*10)+3
    def Add4(event=None):
        if fplus==0:
            ad1=(ad3*10)+4
            ad3=ad1
        else:
            ad2=(ad2*10)+4
    def Add5(event=None):
        if fplus==0:
            ad1=(ad3*10)+5
            ad3=ad1
        else:
            ad2=(ad2*10)+5
    def Add6(event=None):
        if fplus==0:
            ad1=(ad3*10)+6
            ad3=ad1
        else:
            ad2=(ad2*10)+6
    def Add7(event=None):
        if fplus==0:
            ad1=(ad3*10)+7
            ad3=ad1
        else:
            ad2=(ad2*10)+7
    def Add8(event=None):
        if fplus==0:
            ad1=(ad3*10)+8
            ad3=ad1
        else:
            ad2=(ad2*10)+8
    def Add9(event=None):
        if fplus==0:
            ad1=(ad3*10)+9
            ad3=ad1
        else:
            ad2=(ad2*10)+9
    def Add0(event=None):
        if fplus==0:
            ad1=(ad3*10)
            ad3=ad1
        else:
            ad2=(ad2*10)
    #
    ris=Label(calc,
              text=ris1, font=("Arial", 13))
    ris.grid(row=0, column=0)
    ad=Label(calc,
             text=ad1, font=("Arial", 13))
    ad4=Label(calc,
              text=ad2, font=("Arial", 13))
    ad.grid(row=0, column=1)
    ad4.grid(row=0, column=2)
    b1=Button(calc,
             text="1", font=("Arial", 13), command=Add1)
    b1.grid(row=3, column=0)
    b2=Button(calc,
             text="2", font=("Arial", 13), command=Add2)
    b2.grid(row=3, column=1)
    b3=Button(calc,
             text="3", font=("Arial", 13), command=Add3)
    b3.grid(row=3, column=2)
    b4=Button(calc,
             text="4", font=("Arial", 13), command=Add4)
    b4.grid(row=2, column=0)
    b5=Button(calc,
             text="5", font=("Arial", 13), command=Add5)
    b5.grid(row=2, column=1)
    b6=Button(calc,
             text="6", font=("Arial", 13), command=Add6)
    b6.grid(row=2, column=2)
    b7=Button(calc,
             text="7", font=("Arial", 13), command=Add7)
    b7.grid(row=1, column=0)
    b8=Button(calc,
             text="8", font=("Arial", 13), command=Add8)
    b8.grid(row=1, column=1)
    b9=Button(calc,
             text="9", font=("Arial", 13), command=Add9)
    b9.grid(row=1, column=2)
    b0=Button(calc,
             text="0", font=("Arial", 13), command=Add0)
    b0.grid(row=4, column=4)
    
    if __name__=="__main__" and fclose!=1:
        calc.mainloop()

def Cerca(event=None):
    testo=search.get()
    ricerca=Tk()
    ricerca.title("Ricerca")
    ricerca.geometry("1000x525")
    ricerca.configure(background="white")
    ricerca.resizable(True, True)
    testi=wikipedia.summary(testo)
    #reac=testi.replace(" ", "\n", 10)
    Informazioni=Label(ricerca,
                       text=reac, font=("Arial", 10),
                       bg="white", fg="black")
    Informazioni.grid(row=0, column=0, sticky="N")

def Nome(event=None):
    Nome=Tk()
    Nome.title("Name")
    

def crea1(event=None):
    print("O")
def crea2(event=None):
    print("WE")

def crea(event=None):    
    New=Label(Main,
              text="New", font=("Arial", 14), fg="blue",
              bg="white")
    New.grid(row=5, column=3, sticky="WE", padx="20")
    cartella=Button(Main,
                    text="Folder", font=("Arial", 13),
                    command=crea1, bg="yellow", fg="red")
    cartella.grid(row=6, column=2, sticky="WE", padx="20")
    programma=Button(Main,
                     text="Project", font=("Arial", 13),fg="yellow",
                     bg="blue", command=crea2)
    programma.grid(row=6, column=3, sticky="WE")
    


Main=Tk()
Main.title("")
Main.geometry("900x800")
Main.configure(background="lime")
Main.resizable(True, True)



        
close=Button(Main,
             text="Q", font=("Arial", 13),
             command=close, bg="red", fg="blue")
close.grid(row=0, column=0, sticky="WE")

calc=Button(Main,
            text="Calc.", bg="blue", fg="yellow",
            font=("Arial",13), command=calcolatore)
calc.grid(row=0, column=1, sticky="WE")


search=Entry()
search.grid(row=0, column=2, sticky="WE")

Main.bind("<Return>", Cerca)


Main.bind("<Button-3>", crea)




find=Button(Main,
            text="Search", font=("Arial", 13),
            bg="green", command=Cerca)
find.grid(row=0, column=3, sticky="WE")

if __name__=="__main__" and fclose!=1:
    Main.mainloop()
