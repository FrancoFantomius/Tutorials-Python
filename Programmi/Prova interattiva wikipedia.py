import wikipedia

fx=input("Inserire il termine da cercare |")

wikipedia.set_lang("it")

wikipedia.summary(fx)

print(wikipedia.summary(fx))

