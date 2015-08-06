from __future__ import division
import nltk, random
from nltk import word_tokenize
import urllib
import numpy as np

url = "http://www.gutenberg.org/cache/epub/3021/pg3021.txt"
response = urllib.urlopen(url)
raw = response.read().decode('utf8')
tokens = word_tokenize(raw)
text = nltk.Text(tokens)
tagged = nltk.pos_tag(text,tagset='universal')
freqs = nltk.FreqDist(tagged)

tags = ('VERB','NOUN','PRON','ADJ','ADV','ADP','CONJ','DET','NUM','PRT','X','.')
probs = {}
words = {}
for tag in tags:
    bigrams = nltk.bigrams(tagged)
    nexts = [b[1] for (a, b) in bigrams if a[1] == tag]
    fdist = nltk.FreqDist(nexts)
    probs[tag] = [fdist.freq(t)/len(nexts) for t in tags]
    words[tag] = [a[0] for a in tagged if a[1] == tag]
tag_prob = [freqs.freq(tag) for tag in tags ]

current_pos = np.random.choice(tags, 1, tag_prob)[0]
current_word = random.choice(words[current_pos])
print(current_word),
while random.randint(0, 20) <> 1:
    current_pos = np.random.choice(tags, 1, probs[current_pos])[0]
    current_word = random.choice(words[current_pos])
    print current_word,
    if random.randint(0, 10) <> 1:
        print

