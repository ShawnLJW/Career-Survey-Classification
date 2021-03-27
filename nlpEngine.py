from autocorrect import Speller
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

newWords = ['youre','u','ur','really','sector','industry','be','being','related','else','xd','probably','work','something','sure','yet','interested','either']
no_spell_check = ['raffle','raffles','eunoia','lasalle','chong']
cStopwords = stopwords.words('english')
cStopwords += newWords
lem = WordNetLemmatizer()
spell = Speller()
punc = re.compile(r"[^a-zA-Z0-9 ]+")

def removePunc(i):
    i = re.sub(r"[.,?!:;]", ' ', i)
    i = punc.sub(' ', i)
    return i

def findKeywords(i):
    try:
        i = removePunc(i)
        i = word_tokenize(i)
        i = pos_tag(i)
        kw = []
        for word,tag in i:
            if word == 'IT':
                kw.append('technology')
            word = word.lower()
            if word[:3] == 'las':
                word = 'lasalle'
            if word not in no_spell_check and len(word)>4:
                word = spell(word)
            if word == 'tech':
                kw.append('technology')
            elif word == 'media':
                kw.append('media')
            elif word not in cStopwords:
                kw.append(lem.lemmatize(word, pos=tag[0].lower() if tag[0].lower() in 'arnv' else 'n'))
        return kw
    except TypeError:
        return []