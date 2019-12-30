import tkinter as tk

def prendi(event=None):
    testo1=text.get()
    print(testo1)    

window=tk.Tk()
window.geometry("900x550")
window.title("Esempio")

window.grid_columnconfigure(0, weight=1)


first=tk.Label(window,
               text="Vedi tu",
               font=("Arial", 20))
first.grid(row=0, column=0, sticky="N", padx=20, pady=20)

text=tk.Entry()
text.grid(row=1, column=0, sticky="WE", padx=10)

button=tk.Button(text="Non so", command=prendi)
button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)



if __name__=="__main__":
    window.mainloop()

