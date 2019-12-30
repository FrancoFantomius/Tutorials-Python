prova=open("download.jpg","rb")
arancia=prova.readlines()
prova.close()

arancia=str(arancia).split("\\")


print (arancia)
