f2=("è", "tua","zia",".","quino")
print (f2)
for fq in f2:
    if fq=="quino":
        break
    print (fq)
    if fq=="tua":
        continue
    print  (fq)
f1=input("Dimmi una parola. ")
fc=1
for fx in f1:
    print(fx,"è la",fc,"° lettera.")
    fc=fc+1
print("La parola",f1,"è lunga caratteri",len(f1))
