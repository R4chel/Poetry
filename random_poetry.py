import nltk, random
from nltk import word_tokenize
import numpy as np

f = open('robertfrost500.txt')
raw = f.read().decode('utf8')
tokens = word_tokenize(raw)
text = nltk.Text(tokens)
full_tagged = nltk.pos_tag(text,tagset='universal')
tagged = [a for a in full_tagged if a[1] not in ['NUM','X','.']]


tags = ('VERB','NOUN','PRON','ADJ','ADV','ADP','CONJ','DET')
probs = {}
words = {}
for tag in tags:
    bigrams = nltk.bigrams(tagged)
    nexts = [b[1] for (a, b) in bigrams if a[1] == tag]
    fdist = nltk.FreqDist(nexts)
    probs[tag] = [fdist.freq(t)/len(nexts) for t in tags]
    words[tag] = list(set(a[0] for a in tagged if a[1] == tag))

freqs = nltk.FreqDist(tagged)
start_prob = [freqs.freq(tag) for tag in tags]

current_pos = np.random.choice(tags, 1, start_prob)[0]
current_word = random.choice(words[current_pos])
print(current_word),
rand_lines = 0
while rand_lines < 3:
    rand_words = 0
    while rand_words < 1:
        current_pos = np.random.choice(tags, 1, probs[current_pos])[0]
        current_word = random.choice(words[current_pos])
        print(current_word),
        rand_words += random.random()
    rand_lines += random.random()
    print
