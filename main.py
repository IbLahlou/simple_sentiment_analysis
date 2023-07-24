from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)