print("Va bene,\n solo alcune precisazioni prima di cominciare:\ntutto ciò che scrivi verrà salvato in un foglio di testo; inoltre sto per aprire un'interfaccia di scrittura")
from tkinter import *

fq=input("Stavi già scrivendo in questo file? ")
if fq=="Sì" or fq=="sì" or fq=="si" or fq=="Si":
  fs1=open("save.txt","r")
  fr=fs1.read()
  print("Questo è quello che hai scritto finora:\n",fr)
  fs1.close()
def fs1 (event=None):
  fl=""
  fr=""
  fc=ft.get(0.0,END)
  fr=fc.split("\n")
  for fl in fr:
          print ("Questo è quello che verrà salvato\n\n",fl)
          fs1=open("save.txt","a")
          fs1.write("\n")
          fs1.write(fl)
          fs1.close()

fs=Tk()
fs.title("Interfaccia di scrittura")
ft=Text(fs,font="Arial")
ft.pack()
fs.bind("<Return>",fs1)
ft["bg"]="#0000ff"
fs.mainloop
