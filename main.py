from newspaper import Article
from textblob import TextBlob


choice = "Y"
if (choice == 'Y'):
    print("Tap the url in the code")
    url = 'https://www.theguardian.com/world/2023/jul/20/auckland-shooting-police-shut-down-cbd-streets-amid-reports-of-gunman'
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    text = article.summary
    print(text)

else :
    print("Tap the path of Which file you want")
    with open('negative_file.txt', 'r') as f:
        text = f.read()

blob = TextBlob(text)
sentiment =blob.sentiment.polarity # - 1 to 1
print(sentiment)

