from tkinter import *

Main=Tk()
Main.title("MaPf")
Main.geometry("700x600")
Main.configure(bg="white")
Main.resizable(True, True)


inizio=Label(Main,
             text="Scegliere la funzione", font=("Arial", 15),
             bg="white")
inizio.grid(row=0, column=1, padx=200)

R=Button(Main,
         text="Q", font=("Bitmap", 15),
         bg="white", fg="blue")
R.grid(row=0, column=2)

E=Button(Main,
         text="R-E", font=("Bitmap", 15),
         bg="white", fg="yellow")
E.grid(row=0, column=0)

P=Button(Main,
         text="Prendi", font=("Arial", 15),
         bg="white", fg="black")
P.grid(row=1, column=0)



if __name__=="__main__":
    Main.mainloop()
