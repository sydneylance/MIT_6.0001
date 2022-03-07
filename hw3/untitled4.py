#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:35:54 2021

@author: sydneylance
"""

# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Sydney Lance
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


hand = {
        'a':1, 'l':3, 'w':2, 
        }
word = 'w*ll'
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
	
word_list = load_words()
# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
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
    

        if 7 * len(word) - 3 * (n - len(word)) <= 1:
            hand_size_score += 1
        else :
            hand_size_score +=  7 * len(word) - 3 * (n - len(word))
        
        total_word_score += letter_score * hand_size_score
    
    return total_word_score
    
    
    
    pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
# def display_hand(hand):
#     """
#     Displays the letters currently in the hand.

#     For example:
#        display_hand({'a':1, 'x':2, 'l':3, 'e':1})
#     Should print out something like:
#        a x x l l l e
#     The order of the letters is unimportant.

#     hand: dictionary (string -> int)
#     """
    
#     for letter in hand.keys():
#         for j in range(hand[letter]): 
#              print(letter, end=' ')      # print all on the same line
#     print()                              # print an empty line

# #
# # Make sure you understand how this function works and what it does!
# # You will need to modify this for Problem #4.
# #
# def deal_hand(n):
#     """
#     Returns a random hand containing n lowercase letters.
#     ceil(n/3) letters in the hand should be VOWELS (note,
#     ceil(n/3) means the smallest integer not less than n/3).

#     Hands are represented as dictionaries. The keys are
#     letters and the values are the number of times the
#     particular letter is repeated in that hand.

#     n: int >= 0
#     returns: dictionary (string -> int)
#     """
    
#     hand={}
#     num_vowels = int(math.ceil(n / 3))

#     for i in range(num_vowels):
#         x = random.choice(VOWELS)
#         hand[x] = hand.get(x, 0) + 1
    
#     for i in range(num_vowels, n):    
#         x = random.choice(CONSONANTS)
#         hand[x] = hand.get(x, 0) + 1
    
#     return hand

#
# Problem #2: Update a hand by removing letters
#
# def calculate_handlen(hand):
#     """ 
#     Returns the length (number of letters) in the current hand.
    
#     hand: dictionary (string-> int)
#     returns: integer
#     """
#     handlen = 0
#     all_lowercase = string.ascii_lowercase
    
#     for letter in hand:
#         if letter in all_lowercase:
#             handlen += hand.get(letter,0)
        
#     return handlen

# print(calculate_handlen(hand))


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word_lower = word.lower() 
    letter_dict = get_frequency_dict(word_lower)
    all_lowercase = string.ascii_lowercase
    wild = '*'
    num = 0
    
    
    if word_lower in word_list:
           
        for letter in word_lower:
            
            if letter in all_lowercase or wild:
           
                if not hand.get(letter,0) >= letter_dict.get(letter,0):
                
                    return False
    
                    
    for i in range(len(word_lower)):
        if (word_lower[i] == '*' in VOWELS) or (word_lower[i] == word[i] in word_list):
            num += 0
        else:
            num += 1
    if num != 0:
        return False
            
    
print(is_valid_word(word, hand, word_list))

if __name__ == '__main__':
    word_list = load_words()
    
    
    
    def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word_lower = word.lower() 
    letter_dict = get_frequency_dict(word_lower)
    all_lowercase = string.ascii_lowercase
    
    
    if word_lower in word_list:
           
        for letter in word_lower:
           
            if not hand.get(letter,0) >= letter_dict.get(letter,0):
                
                return False
        
        return True
            
    else:
        return False 
    
    
    
    
    
    
    
    
    
    
    
        