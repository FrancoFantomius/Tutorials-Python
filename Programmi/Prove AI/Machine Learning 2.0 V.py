fc=open("comands.txt","r")
ft=fc.readlines()
fc.close()
fdom=input("- ")
for fq in range(0,len(ft),2):
    if (fdom)==(ft[fq][:-1]):
        print(ft[fq+1][:-1])
        break
