from tkinter import *


conf=open("config.ccg","r")
config=conf.readlines()
conf.close()

fb=config[1][:-2]

fplus=0

ad1=0
ad2=0
ad3=ad1

f7=0

Main=Tk()
Main.title("")
Main.geometry("900x800")
Main.configure(background=fb)
Main.resizable(True, True)


ris1=0
fclose=0
flog=0

def close(event=None):
    fclose=1

def nome(cosa, nome):
    fe=("Write here the name of the new",cosa)
    rinom=Tk()
    rinom.title("Rinomina")
    rinom.geometry("300x200")
    rinom.configure(bg="white")
    rinom.resizable(False, False)
    presentazione=Label(rinom,
                        text=fe, font=("Arial", 15),
                        bg="grey")
def calcolatore(event=None):
    print("WIP")

def Cerca(event=None):
    import wikipedia
    wikipedia.set_lang("it")
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
    



def crea(event=None):
    def Bg(event=None):
        BG=Tk()
        BG.title("")
        BG.geometry("300x200")
        def write(colore):
            conf=open("config.txt","r")
            config=conf.readlines()
            conf.close()
            conf=open("config.txt","w")
            confi=config[0]
            conf.write(str(confi))
            if colore==0:
                confi="red"
            if colore==1:
                confi="green"
            if colore==2:
                confi="blue"
            if colore==3:
                confi="lightblue"
            if colore==4:
                confi="lime"
            if colore==5:
                confi="cyan"
            if colore==6:
                confi="white"
            if colore==7:
                confi="black"
            conf.write(confi)
            confi=config[2:]
            conf.write(str(confi))
            conf.close()
            conf=open("config.txt","r")
            config=conf.readlines()
            conf.close()
            print(confi)
                
        R=Button(BG,
                 text="Red", font=("Arial",13),
                 bg="red",command=write(0))
        R.grid(row=0, column=0, sticky="WE")
        G=Button(BG,
                 text="Green", font=("Arial",13),
                 bg="green",command=write(colore=1))
        G.grid(row=0, column=1, sticky="WE")
        B=Button(BG,
                 text="Blue", font=("Arial",13),
                 bg="blue",command=write(colore=2))
        B.grid(row=0, column=2, sticky="WE")
        LB=Button(BG,
                 text="LightBlue", font=("Arial",13),
                 bg="lightblue",command=write(colore=3))
        LB.grid(row=1, column=0, sticky="WE")
        L=Button(BG,
                 text="Lime", font=("Arial",13),
                 bg="lime",command=write(colore=4))
        L.grid(row=1, column=1, sticky="WE")
        C=Button(BG,
                 text="Cyan", font=("Arial",13),
                 bg="cyan",command=write(colore=5))
        C.grid(row=1, column=2, sticky="WE")
        W=Button(BG,
                 text="White", font=("Arial",13),
                 bg="white",command=write(colore=6))
        W.grid(row=2, column=0, sticky="WE")
        B=Button(BG,
                 text="Black", font=("Arial",13),
                 bg="black", fg="white", command=write(colore=7))
        B.grid(row=2, column=1, sticky="WE")
    Add=Optionmenu(Main)
    Add.grid(row=1, column=8)
    BG=Button(Add,
              text="Background", font=("Arial", 13),
              bg="lime", command=Bg)
    #BG.grid(row=0, column=0)





        
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


agg=Button(Main,
           text="+", font=("Arial",13),
           bg="lime", fg="red", command=crea)
agg.grid(row=0, column=9, sticky="N")




find=Button(Main,
            text="Search", font=("Arial", 13),
            bg="green", command=Cerca)
find.grid(row=0, column=3, sticky="WE")

if __name__=="__main__" and fclose!=1:
    Main.mainloop()
