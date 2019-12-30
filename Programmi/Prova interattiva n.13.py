fd=open("Quiz.txt","r")
ft=fd.readlines()
fp=0
for fx in range(0,len(ft),2):
    fdom=input(ft[fx])
    if fdom==ft[fx+1][:-1]:
        print("Giusto")
        fp=fp+1
    else:
        print("Sbagliato")
        print("La tua risposta è '",fdom,"' ma la risposta giusta a questa domanda è:'",ft[fx+1][:-1],"'.")
fd.close()
print(fp)
