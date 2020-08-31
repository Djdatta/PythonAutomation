'''
Created on Aug 28, 2020

@author: Dattatray.Jadhav
'''
from _hashlib import new
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
#print(words)    #['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
print(newlist)
newlist.append(15)
newlist.append(12)
newlist.append(13)
newlist.append(14)
print(newlist)
#newlist.clear()
print(newlist.count(12))
print(newlist)
newlist.remove(12)
print(newlist)
newlist.sort(key=None, reverse=False)
newlist.insert(0, 17)
print(newlist)
print(newlist)