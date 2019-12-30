fmassimo=0
fvalori=0
while fvalori!="fine":
    fvalori=input("-")
    fmem=open("Schema.txt","a")
    fmem.write(fvalori)
    fmem.write("\n")
    fmem.close()
    fmassimo=fmassimo+1
print(fmassimo)
