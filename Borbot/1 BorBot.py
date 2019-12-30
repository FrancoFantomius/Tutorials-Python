fs=open("savedata.txt","r")
fv1=fs.readlines()
fq=""
fs.close()
for fx in range(0,len(fv1),2):
    fnom=(fv1[1][:-2])
    if fnom=="[null]":
        fnom=input("Posso sapere qual'è il tuo nome?")
        print ("Va bene, ",fnom,", che bel nome!")
        fs=open("savedata.txt","r")
        fv1=fs.read()
        fs=open("savedata.txt","w")
        fs.write("fnom:\n")
        fs.close
        fv2=fv1[14:]
        fs=open("savedata.txt","a")
        fs.write(fnom)
        fs.write(".\n")
        fs.write(fv2)
        fs.close()
else:
    print("Ciao ",fnom)
fs=open("savedata.txt","r")
fv1=fs.readlines()
fsat=(fv1[2][:-2])
fs.close()
if fsat=="[null]":
    f+=0
fd=input("Di cosa vuoi parlare?\n")

fc=open("comands.txt","r")
ft=fc.readlines()
fc.close()
fe=0
ff=0
while fd!="fine":
    fd=fd.capitalize()
    if fd=="Regole":
        print("Dato che me lo chiedi ti diro i miei criteri per intrattenere una conversazione con te:")
        print("1- Io sono programmato per parlare con una sola persona per computer, infatti salvo le impostazioni più importanti in un unico file")
        print("2- Per favore, non usare un linguaggio scurrile; dal momento che non lo capirei e non avrebbe senso")
        print("3- Posso imparare da te, perciò puoi aggiungermi nuove possibilità di discussioni")
        print("4- Uso un parametro di soddisfazione per regolare i miei dialoghi, quindi ti esorto ad usare emoticon, per la lista digita 'emoticon'")
        print("5- Per parlare non è necessario aggiungere '!' all'inizio di ogni frase")
        ff=1
        fe=1
    if fd=="Addizioni":
           fnum=input("Dimmi qual'è il primo numero ")
           fnum1=input("Dimmi qual'è il secondo numero ")
           print("La somma tra",fnum,"e",fnum1,"è",fnum+fnum1,".")
           ff=1
           fe=1
    if fd=="Sottrazioni":
           fnum=eval(input("Dimmi qual'è il primo numero "))
           fnum1=eval(input("Dimmi qual'è il secondo numero "))
           print("La differenza tra",fnum2,"e",fnum3,"è",fnum2-fnum3,".")
           ff=1
           fe=1
    if fd=="Moltiplicazioni":
           fnum=eval(input("Dimmi qual'è il primo numero "))
           fnum1=eval(input("Dimmi qual'è il secondo numero "))
           print("Il prodotto tra",fnum4,"e",fnum5,"è",fnum4*fnum5,".")
           ff=1
           fe=1
    if fd=="Divisioni":
           fnum=eval(input("Dimmi qual'è il primo numero "))
           fnum1=eval(input("Dimmi qual'è il secondo numero "))
           print("Il quoto tra",fnum6,"e",fnum7,"è",fnum6/fnum7,"ovviamente senza resto.")
           ff=1
           fe=1
    if fd=="Italiano":
        fp=input("Dimmi qualcosa (anche più di una parola) ")
        fs=eval(input("Quale numero preferisci? "))
        print ("Il numero",fs,"corrisponde alla lettera",fp[fs],"di",fp)
        print ("Le lettere da",fp[fs],"a",fp[fs+2],"sono",fp[fs:fs+2])
        ff=1
        fe=1
    if fd=="Lista":
        print("Va bene, ricorda solo che è ancora da sviluppare completamente.")
        fl=input("Dimmi gli oggetti nella tua lista, dividendoli con degli spazi. ")
        fdomanda=input("Cosa vuoi che ne faccia? Controllare se qualcosa è presente oppure riditela?")
        if (fdomanda=="Controlla se c'è qualcosa" or fdomanda=="Controlla"):
                 fq1=input("Cosa vuoi che controlli? ")
                 print("Va bene,",fq1,"è presente",fl.count(fq1),"volta")
                 ff=1
                 fe=1
        if (fdomanda=="Ripetila" or fdomanda=="ridimmela" or fdomanda=="ripetimi la lista" ):
            print("Ecco la tua lista ",fl)
            ff=1
            fe=1
    for fq in range(0,len(ft),2):
        if (fd)==(ft[fq][:-1]):
            print(ft[fq+1][:-1])
            ff=1
            fe=1
            break
    for fq in range(0,len(ft),2):
        if fe==0:
            fr=input("Dato che la risposta non figura nelle mie banche dati, potresti dirmi cosa risponderesti al mio posto?\n")
            fs=input("Vuoi che cambi alcune parole di quello che mi hai detto?\n")
            fs=fs.capitalize()
            if fs=="Sì" or fs=="Si" or fs=="Va bene":
                fr=fr.replace("giorno","dì")
                fr=fr.replace("casa","dimora")
                fr=fr.replace("parte","pezzo")
            else:
                print("Va bene")
            fc=open("comands.txt","a")
            fc.write(fd.capitalize())
            fc.write("\n")
            fc.write(fr.capitalize())
            fc.write("\n")
            fc.close()
            print("Questo è quello che è stato salvato:\n",fr)
            fc=open("comands.txt","r")
            ft=fc.readlines()
            fc.close()            
            ff=1
            fe=0
            break
        else:
            fe=0
            break
    if ff==1:
        fd=input("Di cosa parliamo adesso?")
