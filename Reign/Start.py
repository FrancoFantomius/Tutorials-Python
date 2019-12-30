def MainMenu():
    import tkinter as tk
    
    begin=tk.Tk()
    begin.geometry("600x600")
    begin.title("Reign")
    begin.configure(background="green")
    
    def firstB():
        print("Ok")
    Play=tk.Button(text="Play", command=firstB)
    Play.grid(row=0,column=0)
    
    if __name=="__main__":
        if fe!=1:
            begin.mainloop()

MainMenu()
