# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:13:02 2021

@author: tarun
"""
from functools import cmp_to_key
letter_score = {}
def assign_score(letters, score):
    for letter in letters.split(','):
        letter_score[letter] = score

# initialize the scores for every letter
assign_score('E,A,O,T,I,N,R,S,L,U', 1)
assign_score('D,G', 2)
assign_score('C,M,B,P', 3)
assign_score('H,F,W,Y,V', 4)
assign_score('K', 5)
assign_score('J,X', 8)
assign_score('Q,Z', 10)

def get_word_score(word):
    return sum([letter_score[w] for w in word])

def compare(a, b):
    s1 = get_word_score(a)
    s2 = get_word_score(b)
    return s2 - s1

# check if all the letters of word are in contains_list
def check_contains(contains_list, word, a, b):
    if b != 0:
        word = word[a:-1 * b]
    else: word = word[a:]
    from collections import defaultdict
    d = defaultdict(lambda: 0)
    for c in contains_list:
        d[c] = d[c] + 1
    for w in word:
        if w in d and d[w] != 0:
            d[w] -= 1
        else:
            return False
    return True

# check which words begin with prefix and the following letters are contained in contains_list
def get_prefix_and_contains(prefix, suffix, contains_list, word_list):
    return [word for word in word_list if word.startswith(prefix) and word.endswith(suffix) and check_contains(contains_list, word, len(prefix), len(suffix))]

word_list = []
with open('dictionary.txt', 'r') as f:
    word_list = [word.rstrip() for word in f]

prefix = input('Enter prefix if any : ').upper()
suffix = input('Enter suffix if any : ').upper()
contains = input('Enter comma separated letters that you have : ').upper()
print(prefix, contains.split(','), suffix)
ls = get_prefix_and_contains(prefix, suffix, contains.split(','), word_list)
print(sorted(ls, key=cmp_to_key(compare)))
