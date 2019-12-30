import tkinter as tk

finestra=tk.Tk()
finestra.geometry("600x500")
finestra.title("Quiz")
finestra.resizable(True, True)
finestra.configure(background="lime")
finestra.grid_columnconfigure(0, weight=1)





















domanda=tk.Label(finestra,
                 text="Ciao",
                 font=("Arial", 15), background="lime")
domanda.grid(row=0, column=0, sticky="WE", padx=20, pady=10)
