fr1=open("fp.txt","r")
fr=fr1.readlines()
print(fr)
for ff in fr:
    print (ff[:-1])

fr1.close()
