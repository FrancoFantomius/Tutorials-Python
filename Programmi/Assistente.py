print ("È consigiliato mettere il programma a schermo intero")
fn=input("Qual è il tuo nome? ")
while fn=="account_prova" or fn!="Francesco":
    print("Per ora non sono disponibili contenuti di questo programma in modalità utente normale.")
    fn=input("Vuoi usare un altro nome? ")
if fn=="Francesco":
    print("Ciao",fn)
    fo=input("Cosa facciamo oggi? ")
    if fo=="Programmiamo":
        print("Mi dispiace, ma non hai ancora un editor :(")
    if fo=="Scriviamo":
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

    if fo=="Calcoliamo":
        print("Va bene")
        fc=input("Quale operazione vuoi eseguire? Addizioni | Sottrazioni | Moltiplicazioni | Divisioni ")
        if fc=="Addizioni":
           fnum=input("Dimmi qual'è il primo numero ")
           fnum1=input("Dimmi qual'è il secondo numero ")
           print("La somma tra",fnum,"e",fnum1,"è",fnum+fnum1,".")
        if fc=="Sottrazioni":
           fnum2=eval(input("Dimmi qual'è il primo numero "))
           fnum3=eval(input("Dimmi qual'è il secondo numero "))
           print("La differenza tra",fnum2,"e",fnum3,"è",fnum2-fnum3,".")
        if fc=="Moltiplicazioni":
           fnum4=eval(input("Dimmi qual'è il primo numero "))
           fnum5=eval(input("Dimmi qual'è il secondo numero "))
           print("Il prodotto tra",fnum4,"e",fnum5,"è",fnum4*fnum5,".")
        if fc=="Divisioni":
           fnum6=eval(input("Dimmi qual'è il primo numero "))
           fnum7=eval(input("Dimmi qual'è il secondo numero "))
           print("Il quoto tra",fnum6,"e",fnum7,"è",fnum6/fnum7,"ovviamente senza resto.")
    if fo=="Italiano":
        fp=input("Dimmi qualcosa (anche più di una parola) ")
        fs=eval(input("Quale numero preferisci? "))
        print ("Il numero",fs,"corrisponde alla lettera",fp[fs],"di",fp)
        print ("Le lettere da",fp[fs],"a",fp[fs+2],"sono",fp[fs:fs+2])
    if fo=="Lista":
        print("Va bene, ricorda solo che è ancora da sviluppare completamente.")
        fl=input("Dimmi gli oggetti nella tua lista, dividendoli con degli spazi. ")
        fdomanda=input("Cosa vuoi che ne faccia? Controllare se qualcosa è presente oppure riditela?")
        if (fdomanda=="Controlla se c'è qualcosa" or fdomanda=="Controlla"):
                 fq1=input("Cosa vuoi che controlli? ")
                 print("Va bene,",fq1,"è presente",fl.count(fq1),"volta")
        if (fdomanda=="Ripetila" or fdomanda=="ridimmela" or fdomanda=="ripetimi la lista" ):
            print("Ecco la tua lista ",fl)
    if fo=="Quiz":
        print("Come disse un mio famoso collega:\n'Sto caricando le domande'")
        
    if fo=="Parliamo":
        print("Sono stato programmato per fare conversazione, ma la mia capacità di linguaggio e di saper rispondere alle domande potrebbe non essere sempre perfetta")
        fd1=input("Di cosa vuoi parlare? ")
        if (fd1=="Di te" or fd1=="Del tuo sviluppo"):
            print("Con piacere, probabilmente ti piacerà sapere che sono nato il 12 Aprile.")
            fd2=input("")
            if (fd2=="Puoi parlarmi ancora di te" or fd2=="Posso saperne di più?"):
                print("Mi dispiace, ma non sono autorizzato a rilasciare ulteriori informazioni.")
                fd3=input("")
            elif (fd3=="Cambiamo discorso" or fd2=="Puoi parlarmi di altro?" or fd2=="Cambiamo discorso" or fd3=="Puoi parlarmi di altro?"):
                print("Ma certamente")
            else:
                fd2=input("Mi dispiace, cambiamo discorso.")
else:
    print("Mi dispiace, ma devo sono ancora in una fase dello sviluppo non ancora pronta per il pubblico.")
