fvalori=0
fpunti=1
fmassimo=0
fmodalità=input("Raccolta | Analisi")
if fmodalità=="Raccolta":
    while fvalori!="fine":
        fvalori=input("-")
        fmem=open("Schema.txt","a")
        fmem.write(fvalori)
        fmem.write("\n")
        fmem.close()
        fmassimo=fmassimo+1
    fmem=open("schema.txt","a")
    fmem.write(fmassimo)
    fmem.close()
if fmodalità=="Analisi":
    fmem=open("Schema.txt","r")
    fanalisi1=fmem.readlines()
    fmassimo=fanalisi1[]
    fanalisi2=fanalisi1[1][:-1]
    fanalisi3=fanalisi1[2:fmassimo][:]#possibile ERROR
    for ftrova in range(0,len(fanalisi3),1):
        if (fanalisi2)==(fanalisi3[ftrova][:-1]):
            fpunti=fpunti+1
    while fpunti!=(fmassimo-1):
        fanalisi2=fanalisi1[fpunti][:-1]
        fanalisi3=fanalisi1[fpunti+1:][:]
        for ftrova in range(0, len(fanalisi3),1):
            if (fanalisi2)==(fanalisi3[ftrova][:-1]):
                fpunti=fpunti+1
                frisultato=1
                print("La comprensione è completa al",(fpunti/fmassimo)*100,"%")
                break
        for ftrova in range(0, len(fanalisi3),1):
            if frisultato!=1:
                print("No result!")
                break
    print("Schema trovato!!")
