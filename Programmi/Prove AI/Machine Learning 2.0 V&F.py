fc=open("comands.txt","r")
ft=fc.readlines()
fc.close()
fdom=input("- ")
fe=0
for fq in range(0,len(ft),2):
    if (fdom)==(ft[fq][:-1]):
        print(ft[fq+1][:-1])
        fe=1
        break
for fq in range(0,len(ft),2):
    if fe==0:
        fr=input("Dimmi la risposta\n")
        fc=open("comands.txt","a")
        fc.write(fdom)
        fc.write("\n")
        fc.write(fr)
        fc.write("\n")
        fc.close()
        fe=0
        break
