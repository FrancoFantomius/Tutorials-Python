from tkinter import *

fo=open("traduttore.txt","r")
traduttore=fo.readlines()
fo.close()



def Invio(event=None):
    testo=text.get(0.0,END)
    testo=testo.split(" ")
    print(testo)
    for fq in range(0,len(traduttore),2):
        for ft in range(0,len(testo),1):
            if ft==(traduttore[fq][:-1]):
                testo=testo.replace(ft,traduttore[fq+1][:-1])
    print(fq)





Main=Tk()
Main.geometry("700x500")
Main.title("Programmatore in Python")
Main.resizable(True, True)
Main.configure(background="cyan")



bott1=Label(Main,
               text="Scrivi quello vuoi programmare",
               fg="lime", font=("Arial",13), background="blue")
bott1.grid(row=0, column=0, padx=200)

scrollbar=Scrollbar(Main)
scrollbar.grid(row=2, column=1)




text=Text(Main, background="white", yscrollcommand=scrollbar.set)
text.grid(row=2, column=0, sticky="WE", pady=10, padx=10)


bott2=Button(Main,
             text="Crea", font=("Arial",15),
             background="blue", command=Invio)

bott2.grid(row=3, column=0, sticky="WE", pady=10, padx=10)


#Main.bind("<Return>", Invio1)

if __name__=="__main__":
    Main.mainloop()







from sklearn import tree


