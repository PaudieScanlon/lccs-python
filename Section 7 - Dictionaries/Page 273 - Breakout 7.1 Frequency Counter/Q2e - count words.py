# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 7.1 

# Count the number of words in a sentence (v2)
sentence = input("Enter a sentence: ")
sent_list = sentence.split()
words = {}
for word in sent_list:
    words[word] = words.get(word, 0) + 1

print(words)
