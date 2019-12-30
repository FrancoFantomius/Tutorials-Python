fs=open("comands.txt","r")
fmem=fs.readlines()
fd=input("Dimmi\n")
fs.close()
fq=0
for fq in range(0,len(fmem),2):
    print(fq)
    if fd!=fmem[fq][:-1]:
        fr=input("La domanda non risulta nelle mie banche dati prego inserire la risposta.\n")
        fs=open("comands.txt","a")
        fs.write("\n")
        fs.write(fd)
        fs.write("\n")
        fs.write(fr)
        fs.close()
        break
    else:
        print(fmem[fq+1][:-1])
        break
