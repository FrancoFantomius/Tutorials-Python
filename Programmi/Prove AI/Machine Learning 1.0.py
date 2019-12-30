fc=open("comands.txt","r")
ft=fc.readlines()
fc.close()
for fq in range(0,len(ft),2):
    fdom=input("- ")
    if (fdom)!=(ft[fq][:-1]):
        fr=input("Dimmi la risposta\n")
        fc=open("comands.txt","a")
        fc.write("\n")
        fc.write(fd)
        fc.write("\n")
        fc.write(fr)
        fc.close()
        break
    if (fdom)!=(ft[fq][:-1]):
        print(ft[fq+1][:-1])
        break
