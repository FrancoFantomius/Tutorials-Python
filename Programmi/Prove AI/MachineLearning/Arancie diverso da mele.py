
print("inizializzazione")

from sklearn import tree

print("acquisizione")
prova=open("download.jpg","rb")
arancia=prova.read()
prova.close()
prova=open("download 1.jpg","rb")
arancia1=prova.read()
prova.close()
prova=open("download 2.jpg","rb")
mela=prova.read()
prova.close()
prova=open("download 3.jpg","rb")
mela1=prova.read()
prova.close()
prova=open("download 4.jpg","rb")
mela2=prova.read()
prova.close()
prova=open("download (5).jpg","rb")
mela3=prova.read()
prova.close()
prova=open("images.jpg","rb")
arancia2=prova.read()
prova.close()
prova=open("images (2).jpg","rb")
arancia3=prova.read()
prova.close()
prova=open("images (3).jpg","rb")
arancia4=prova.read()
prova.close()
prova=open("images (4).jpg","rb")
mela4=prova.read()
prova.close()
prova=open("images (6).jpg","rb")
mela5=prova.read()
prova.close()
prova=open("images (1).jpg","rb")
arancia5=prova.read()
prova.close()

print("pre-elaborazione")
arancia=str(arancia).split("\\")
arancia1=str(arancia1).split("\\")
arancia2=str(arancia2).split("\\")
arancia3=str(arancia3).split("\\")
arancia4=str(arancia4).split("\\")
arancia5=str(arancia5).split("\\")

mela=str(mela).split("\\")
mela1=str(mela1).split("\\")
mela2=str(mela2).split("\\")
mela3=str(mela3).split("\\")
mela4=str(mela4).split("\\")
mela5=str(mela5).split("\\")

prova=open("Prova.jpg","rb")
Prova=prova.read()
prova.close()
Prova=str(Prova).split("\\")



fsodd=0
flin=1


rex=open("num.txt","r")
testo=rex.read()
rex.close

fsadd=0

print("analisi")
while fsadd==0:
    for fq in range(0, len(arancia)):#da cambiare
        for ft in range(0,len(testo),2):
            if fq==(testo[ft][:-1]):
                fsodd=1
                fw=open("arancie.txt","w")#da cambiare
                fw.write(testo[ft+1][:-1])
                fw.write(" ")
                fw.close
                break
        for ft in range(0,len(testo),2):
            if fsodd==0:
                add=open("num.txt","a")
                add.write(str(fq))
                add.write("\n")
                add.write(str(flin))
                add.write("\n")
                add.close()
                flin=flin+1
                read=open("num.txt","r")
                testo=read.readlines()
                read.close
                break
    print("Ok")
    for fq in range(0, len(arancia1)):#da cambiare
        for ft in range(0,len(testo),2):
           if fq==(testo[ft][:-1]):
               fsodd=1
               fw=open("arancie1.txt","a")#da cambiare
               fw.write(testo[ft+1][:-1])
               fw.write(" ")
               fw.close
               break
        for ft in range(0,len(testo),2):
           if fsodd==0:
               add=open("num.txt","a")
               add.write(str(fq))
               add.write("\n")
               add.write(str(flin))
               add.write("\n")
               add.close()
               flin=flin+1
               read=open("num.txt","r")
               testo=read.readlines()
               read.close
               break
    print("Ok")
    for fq in range(0, len(arancia2)):#da cambiare
        for ft in range(0,len(testo),2):
           if fq==(testo[ft][:-1]):
               fsodd=1
               fw=open("arancie2.txt","a")#da cambiare
               fw.write(testo[ft+1][:-1])
               fw.write(" ")
               fw.close
               break
        for ft in range(0,len(testo),2):
           if fsodd==0:
               add=open("num.txt","a")
               add.write(str(fq))
               add.write("\n")
               add.write(str(flin))
               add.write("\n")
               add.close()
               flin=flin+1
               read=open("num.txt","r")
               testo=read.readlines()
               read.close
               break
        print("Ok")
    for fq in range(0, len(arancia3)):#da cambiare
        for ft in range(0,len(testo),2):
           if fq==(testo[ft][:-1]):
               fsodd=1
               fw=open("arancie3.txt","a")#da cambiare
               fw.write(testo[ft+1][:-1])
               fw.write(" ")
               fw.close
               break
        for ft in range(0,len(testo),2):
           if fsodd==0:
               add=open("num.txt","a")
               add.write(str(fq))
               add.write("\n")
               add.write(str(flin))
               add.write("\n")
               add.close()
               flin=flin+1
               read=open("num.txt","r")
               testo=read.readlines()
               read.close
               break
        print("Ok")
    for fq in range(0, len(arancia1)):#da cambiare
        for ft in range(0,len(testo),2):
           if fq==(testo[ft][:-1]):
               fsodd=1
               fw=open("arancie1.txt","a")#da cambiare
               fw.write(testo[ft+1][:-1])
               fw.write(" ")
               fw.close
               fsadd=1
               break
        for ft in range(0,len(testo),2):
           if fsodd==0:
               add=open("num.txt","a")
               add.write(str(fq))
               add.write("\n")
               add.write(str(flin))
               add.write("\n")
               add.close()
               flin=flin+1
               read=open("num.txt","r")
               testo=read.readlines()
               read.close
               break



print("Lettura")


arancie=open("arancie.txt")
arancia=str(arancie.read)
arancie.close
arancia=arancia.split(" ")



arancie=open("arancie1.txt")
arancia1=str(arancie1.read )
arancie.close
arancia1=arancia1.split(" ")


arancie=open("arancie2.txt")
arancia2=str(arancie2.read)
arancie.close
arancia2=arancia2.split(" ")



arancie=open("arancie3.txt")
arancia3=str(arancie3.read)
arancie.close
arancia3=arancia3.split(" ")


arancie=open("arancie4.txt")
arancia4=str(arancie4.read)
arancie.close
arancia4=arancia4.split(" ")


arancie=open("arancie5.txt")
arancia5=str(arancie5.read)
arancie.close
arancia5=arancia5.split(" ")


arancie=open("mela.txt")
mela=str(arancie.read)
arancie.close
mela=mela.split(" ")

arancie=open("mela1.txt")
mela1=str(arancie.read)
arancie.close
mela1=mela1.split(" ")

arancie=open("mela2.txt")
mela2=str(arancie.read)
arancie.close
mela2=mela2.split(" ")

arancie=open("mela3.txt")
mela3=str(arancie.read)
arancie.close
mela3=mela3.split(" ")

arancie=open("mela4.txt")
mela4=str(arancie.read)
arancie.close
mela4=mela4.split(" ")

arancie=open("mela5.txt")
mela5=str(arancie.read)
arancie.close
mela5=mela5.split(" ")


arancie=open("Prova.txt")
Prova=str(arancie.read)
arancie.close
Prova=Prova.split(" ")






print("Comprensione")








caratteristiche=[arancia,arancia1,arancia2,arancia3,arancia4,arancia5,mela,mela1,mela2,mela3,mela4,mela5]
frutto=[1,1,1,1,1,1,2,2,2,2,2,2]


classificatore=tree.DecisionTreeClassifier()
classificatore=classificatore.fit(caratteristiche,frutto)



print (classificatore.predict([[Prova]]))
