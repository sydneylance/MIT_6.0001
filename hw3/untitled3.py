#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:22:46 2021

@author: sydneylance
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:53:08 2021

@author: sydneylance
"""

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
word = 'Was'
n = 5






def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    word_lower = word.lower() 
    
    
    letter_score = 0
    hand_size_score = 0
    total_word_score = 0
   
    
    if word_lower in load_words():
        for i in range(len(word)):
        
            if word_lower[i] in SCRABBLE_LETTER_VALUES:
                letter_score += SCRABBLE_LETTER_VALUES[word_lower[i]]
    return letter_score


    #     if 7 * len(word) - 3 * (n - len(word)) <= 1:
    #         hand_size_score += 1
    #     else :
    #         hand_size_score +=  7 * len(word) - 3 * (n - len(word))
        
    #     total_word_score += letter_score + hand_size_score
    
    # return total_word_score
    

print (get_word_score(word, n))
    
#     if 7 * len(word) - 3 * (n - len(word)) <= 1:
#         hand_size_score += 1
#     else:
#        hand_size_score +=  7 * len(word) - 3 * (n - len(word)) 
        
#     total_word_score = letter_score + hand_size_score
#     print(letter_score)
#     print(hand_size_score)
    
#     return total_word_score

# print(get_word_score(word, n))