fc=open("comands.txt","r")
ft=fc.readlines()
fc.close()
fe=0
ff=0
fd=input("Di cosa vuoi parlare?\n")
while fd!="fine":
    if fd=="regole" or fd=="!regole":
        print("Dato che me lo chiedi ti diro i miei criteri per intrattenere una conversazione con te:")
        print("1- Io sono programmato per parlare con una sola persona per computer, infatti salvo le impostazioni più importanti in un unico file")
        print("2- Per favore, non usare un linguaggio scurrile; dal momento che non lo capirei e non avrebbe senso")
        print("3- Posso imparare da te, perciò puoi aggiungermi nuove possibilità di discussioni")
        print("4- Uso un parametro di soddisfazione per regolare i miei dialoghi, quindi ti esorto ad usare emoticon, per la lista digita 'emoticon'")
        print("5- Per parlare non è necessario aggiungere '!' all'inizio di ogni frase")
        ff=1
    else:
        for fq in range(0,len(ft),2):
            if (fd)==(ft[fq][:-1]) and ff!=1:
                print(ft[fq+1][:-1])
                ff=1
                fe=1
                break
        for fq in range(0,len(ft),2):
            if fe==0 and ff!=1:
                fr=input("Dato che la risposta non figura nelle mie banche dati, potresti dirmi cosa risponderesti al mio posto?\n")
                fc=open("comands.txt","a")
                fc.write(fd)
                fc.write("\n")
                fc.write(fr)
                fc.write("\n")
                fc.close()
                ff=1
                fe=0
                break
    if ff==1:
        fd=input("Di cosa parliamo adesso?")
