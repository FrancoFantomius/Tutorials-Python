import math as mt
import random as rd

rd.seed(1)

a4=34
a5=45


def RN(m1,m2):
    w1 = rd.random()
    w2 = rd.random()
    b = rd.random()  
    t=m1*w1+m2*w2+b 
    return sigmoide(t)

def sigmoide(t):
    return 1/(1+mt.exp(-t))


b1=RN(a4,a5)

a=0



while a<=10:
    b1=RN(a4,a5)
    b2=RN(b1, rd.random())
    if b2>=0.73:
        print("Ok", b2)
    a=a+1







b2=RN(a4,a5)
b3=RN(a4,a5)
b4=RN(a4,a5)
b5=RN(a4,a5)
b6=RN(a4,a5)
b7=RN(a4,a5)
b8=RN(a4,a5)
b9=RN(a4,a5)
b0=RN(a4,a5)
