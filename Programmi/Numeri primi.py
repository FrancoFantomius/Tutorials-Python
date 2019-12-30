fe=eval(input("Numero | "))
while fe!=100000000:
    fx=1
    fs=0
    while fx!=fe and fs==0:
        fx=fx+1
        fq=(fe/fx)
        fz=int(fq)
        if fz==fq:
            fs=0
            break
        else:
            fs=1
    if fs==1:
        print(fe,"è un numero primo.")
    if fs==0:
        print(fe,"non è un numero primo.")

    memoria=open("Numeri primi.txt","a")
    memoria.write(str(fe))
    memoria.write("\n")
    memoria.close
    fe=fe+1
