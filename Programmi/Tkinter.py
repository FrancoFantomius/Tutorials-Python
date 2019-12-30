import tkinter as tk
import tkinter.messagebox

window =tk.Tk()
window.geometry("600x600")
window.title("Interfecia")
#window.resizable(False, False)
window.configure(background="white")

def inr():
    text1="Ciao"
    text_output=tk.Label(window, text=text1, fg="red", font=("Arial",12))
    text_output.grid(row=0, column=1)

def inr1():
    text1="Ciao, di nuovo!"
    text_output=tk.Label(window, text=text1, fg="green", font=("Arial",12))
    text_output.grid(row=1, column=1, padx=100)

def Mao():
    tkinter.messagebox.showinfo("window", "PEI")
    answer=tkinter.messagebox.askquestion("Q1", "er")
    if answer=="yes":
        print("OK")


def UNO():
    print("!")

button=tk.Button(text="Salve", command=inr)
button.grid(row=0, column=0)

button1=tk.Button(text="1", command=inr1)
button1.grid(row=1, column=0,pady=20)

cB=tk.Checkbutton(text="CIAO",
                  command=Mao)
cB.grid(row=2, column=0)

me=tk.Menu(window)
window.config(menu=me)

SB=tk.Menu(me)
me.add_cascade(label="WE", me=SB)

SB.add_command(label="wer", command=UNO)
SB.add_separator()
SB.add_command(label="Wer", command=UNO)

EM=tk.Menu(me)
me.add_cascade(label="WERT", menu=EM)
EM.add_command(label="werffh", command=UNO)

toolbar=tk.Frame(window, bg="blue")
IB=tk.Button(toolbar, text="vgjh", command=UNO)
IB.grid(row=0, column=0, padx=2, pady=2)
toolbar.grid(row=6, column=0)



status=tk.Label(window, text="file saved", bd=1)
status.grid(row=5, column=0)

if __name__ == "__main__":
    window.mainloop()
