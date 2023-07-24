from newspaper import Article
from textblob import TextBlob

url = 'https://www.theguardian.com/world/2023/jul/20/auckland-shooting-police-shut-down-cbd-streets-amid-reports-of-gunman'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment =blob.sentiment.polarity # - 1 to 1
print(sentiment)

