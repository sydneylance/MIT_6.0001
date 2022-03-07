#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:34:32 2021

@author: sydneylance
"""



import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 9
n = HAND_SIZE

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

hand = {
        'e': 1, 'a': 1, '*': 1, 'j': 1, 'j': 1, 'r': 1, 'y': 1
        }
word = 'a*r'
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

word_list = load_words()



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

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]): 
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

	
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    wild = '*'
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
     
    hand[wild] = hand.get(wild, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

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
    list_word = list(word_lower)
    possible_words= []
    letter_dict = get_frequency_dict(word_lower)
    wild = '*'
    valid_words = []
    
    #creating list of possible words if wild is present
    if wild in list_word:
      position = list_word.index('*')
      for letter in VOWELS:
          list_word[position] = letter
          possible_words.append("".join(list_word))
    else:
        possible_words.append(word_lower)
   
    #creating list of words in word list
    for w in possible_words:
        print(possible_words)
        if w in word_list:
            valid_words.append(w)
            print(valid_words)
    
    #confirming if the hand contains the letters necessary to generate the word played
    if len(valid_words) >= 1:
        for letter in word_lower:
            if not hand.get(letter,0) >= letter_dict.get(letter,0):
                print(hand.get(letter,0))
                print(letter_dict.get(letter,0))
                return False
        else:
            return True
    
    else:
        return False
    
print(is_valid_word(word, hand, word_list))

# print(deal_hand(n))

# def play_hand(hand, word_list):

#     """
#     Allows the user to play the given hand, as follows:

#     * The hand is displayed.
    
#     * The user may input a word.

#     * When any word is entered (valid or invalid), it uses up letters
#       from the hand.

#     * An invalid word is rejected, and a message is displayed asking
#       the user to choose another word.

#     * After every valid word: the score for that word is displayed,
#       the remaining letters in the hand are displayed, and the user
#       is asked to input another word.

#     * The sum of the word scores is displayed when the hand finishes.

#     * The hand finishes when there are no more unused letters.
#       The user can also finish playing the hand by inputing two 
#       exclamation points (the string '!!') instead of a word.

#       hand: dictionary (string -> int)
#       word_list: list of lowercase strings
#       returns: the total score for the hand
      
#     """
    
#     print("Current Hand:", display_hand(hand))
    
#     word = input('Enter word, or "!!" to indicate that you are finished:')
    
#     if word == '!!':
#         break
#     else:
#         if is_valid_word(word, hand, word_list) == True:
            
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

# print(display_hand(hand))
#
# def is_valid_word(word, hand, word_list):
#     """
#     Returns True if word is in the word_list and is entirely
#     composed of letters in the hand. Otherwise, returns False.
#     Does not mutate hand or word_list.
   
#     word: string
#     hand: dictionary (string -> int)
#     word_list: list of lowercase strings
#     returns: boolean
#     """

#     word_lower = word.lower() 
#     list_word = list(word_lower)
#     possible_words= []
#     letter_dict = get_frequency_dict(word_lower)
#     wild = '*'
#     valid_words = []
    
    
    
#     if wild in list_word:
#       position = list_word.index('*')
#       for letter in VOWELS:
#           list_word[position] = letter
#           possible_words.append("".join(list_word))
#     else:
#         possible_words.append(word_lower)
   
#     for w in possible_words:
#         if w in word_list:
#             valid_words.append(w)
#             print(valid_words)
    
#     if len(valid_words) >= 1:
#         for letter in word_lower:
#             if not hand.get(letter,0) >= letter_dict.get(letter,0):
#                 return False
#         else:
#             return True
    
#     else:
#         return False
        
         # if not in_word_list:
    #     print('in word list loop')
    #     return False
        
    
        # else: 
        #     return True

    
    # for word in word_list:
    #     if len(word_lower) == len(word):
    #         for i in range(len(word_lower)):
    #             if (word_lower[i] == wild) or (word_lower[i] == word[i]):
    #                 if word_lower[wild] in VOWELS:
    #                     num += 0
    #                 else:
    #                     num += 1
    #         if num == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    # for letter in word_lower:                
    #    if letter == wild:
                
                
    #                 return False
    
    # for word in word_list:
            
    #     for i in range(len(word_lower)):
            
    #         # if not hand.get(wild,0) <= 1 or :
    #             if (word_lower[i] == wild) or (word_lower[i] == word[i]):
    #                 if wild in VOWELS and letter_dict[wild] <= 1:
    #                     num += 0
    #                 else:
    #                     num += 1
    #     if num != 0:
    #         return False
            
    
# print(is_valid_word(word, hand, word_list))

if __name__ == '__main__':
    word_list = load_words()
    
    
    
    # def is_valid_word(word, hand, word_list):
    # """
    # Returns True if word is in the word_list and is entirely
    # composed of letters in the hand. Otherwise, returns False.
    # Does not mutate hand or word_list.
   
    # word: string
    # hand: dictionary (string -> int)
    # word_list: list of lowercase strings
    # returns: boolean
    # """

    # word_lower = word.lower() 
    # list_word = list(word_lower)
    # possible_words= []
    # letter_dict = get_frequency_dict(word_lower)
    # wild = '*'
    
    
    
    # if wild in list_word:
    #   position = list_word.index('*')
    #   for letter in VOWELS:
    #       list_word[position] = letter
    #       possible_words.append("".join(list_word))
    # else:
    #     possible_words.append(word_lower)
    
    # in_word_list = False
    # for w in possible_words:
    #     if w not in word_list:
    #         possible_words.remove(w)
    # if len(possible_words) >= 1:
    #     in_word_list = True 
    # if not in_word_list:
    #     return False
           
    # for letter in word_lower:
    #     if not hand.get(letter,0) >= letter_dict.get(letter,0):
    #         return False
    #     else:
    #         return True
    
    
