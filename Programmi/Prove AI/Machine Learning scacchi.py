fx=0
fx1=input("Imparare o eseguire?  ")
fx1.capitalize()
if fx1=="Imparare":
    while fx!="fine":
        fx=input("Mossa | A | D | S |")
        if fx=="A":
            fi=open("scacchi.txt","a")
            fi.write("1")
            fi.close()
        if fx=="D":
            fi=open("scacchi.txt","a")
            fi.write("2")
            fi.close()
        if fx=="S":
            fi=open("scacchi.txt","a")
            fi.write("3")
            fi.close()
    fi=open("scacchi.txt","r")
    ft=fi.read()
    fi.close()
if fx1=="Eseguire":
    fi=open("scaccchi.txt","r")
    fmem=fi.readlines()
    fi.close()
    print()
