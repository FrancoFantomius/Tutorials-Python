import newspaper

news=input("Inserire URL")

fx=newspaper.Article(news)

fx.download()
fx.parse()




print("Titolo | ",fx.title)

print("Testo | ",fx.text)

print("Codice HTML | ",fx.html)

print("Meta data | ",fx.meta_data)

print("Data di pubblicazione | ",fx.publish_date)

print("Sommario | ",fx.summary)

print("Autori | ",fx.authors)
