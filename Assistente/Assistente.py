que=input("Buongiorno signore, cosa vuole che faccia?\n")

risp=open("Form.bbt", "r")
formule=risp.readlines()
risp.close

ris=0



while ris!=1:
    que=que.lower()
    for tut in range(0,len(formule),2):
        tut=tut[:-1]
        print(tut)
    que=input("<->")
