from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import urllib
import ssl

quote_page = 'https://goo.gl/BDB6bE'
page = urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')

import nltk
words = nltk.word_tokenize(soup)
'my_bigrams = nltk.bigrams(words)'
'my_trigrams = nltk.trigrams(words)'
'''
def ngram_probs(filename='raw_sentences.txt'):
    return bigram_probs, trigram_probs

cnt2, cnt3 = ngram_probs()
print(cnt2[('we', 'are')])
'''
