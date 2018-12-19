# Se connecter a Twitter
# Recuperer le dernier Tweet poste
# Executer la commande
# Envoyer l'eventuel resultat sur pastebin

from lxml import html
from urllib2 import urlopen
import bs4

def loadLastTweet():
    webPage = urlopen('https://twitter.com/BrissardGaetan').read()
    webHtml = bs4.BeautifulSoup(webPage)
    webHtml = html.fromstring(webHtml)
    webClass = webHtml.find_class('TweetTextSize')
    print webClass

def main():
    while True:
        print

loadLastTweet()