from tkinter import *

master = Tk()
def OK(re):
    print("KO")
    
listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")
listbox.bind ( "<Button-1>" , OK)
#items = map (int, list.curselection ())

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
mainloop()
