from tkinter import *

conf=open("config.wup", "r")
config=conf.readlines()
conf.close()

title=config[1][:-1]
backd=config[3][:-1]
log=config[5][:-1]


Main=Tk()
Main.geometry("900x800")
Main.title(str(title))
Main.configure(bg=backd)
Main.resizable(True, True)

if str(log)=="0":
    war=Label(Main,
              text="Effetua il LogIn", font=("Arial", 13),
              fg="red")
    war.grid(row=1, column=9)

def crea(event=None):
    None

def Log(event=None):
    def invio(event=None):
        nome=Name.get()
        password=Pass.get()
        conf=open("config.wup", "r")
        config=conf.readlines()
        conf.close()
                    
        if nome=="":
            Att=Label(log,
                      text="IMMETTI I TUOI DATI", font=("Arial", 15),
                      fg="red")
            Att.grid(row=5, column=0)
        if password=="":
            Att=Label(log,
                      text="IMMETTI I TUOI DATI", font=("Arial", 15),
                      fg="red")
            Att.grid(row=5, column=0)
        da=open("dati.wup", "r")
        dati=da.readlines()
        dati=dati[:][:-1]
        da.close()
        for name in range(0,len(dati),2):
            if name==nome:
                if dati[name+1][:-1]==password:
                    flog=1
                    
                    conf=open("config.wup", "w")
                    conf.write(config[:4])
                    conf.write("1\n")
                    conf.write(name)
                    conf.write("\n")
                    conf.close()

    log=Tk()
    log.geometry("350x200")
    log.title("LogIn")
    log.configure(bg="white")
    log.resizable(False, False)
    q=Label(log,
            text="Prego inserire il nome utente", font=("Arial", 14),
            fg="blue", bg="white")
    q.grid(row=0, column=0)
    Name=Entry(log)
    Name.grid(row=1, column=0)
    w=Label(log,
            text="Immetti la tua password", font=("Arial", 14),
            fg="blue", bg="white")
    w.grid(row=2, column=0)
    Pass=Entry(log)
    Pass.grid(row=3, column=0)
    Invia=Button(log,
                 text="LogIn", font=("Arial", 14),
                 fg="blue", bg="white", command=invio)
    Invia.grid(row=4, column=1)


B1=Button(Main,
          text="+", font=("Arial", 15),
          fg="green", bg="#0fdb76", command=crea)
B1.grid(row=0, column=1)

if str(log)=="1":
    compl="Benvenuto, "+config[6][:-1]
    L0=Label(Main,
             text=compl, font=("Arial", 15))
    L0.grid(row=0, column=0)

B9=Button(Main,
          text="LogIn", font=("Arial", 15),
          bg="green", command=Log)
B9.grid(row=0, column=9)


if __name__=="__main__":
    Main.mainloop()
