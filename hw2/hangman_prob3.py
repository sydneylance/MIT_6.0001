#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:55:07 2021

@author: sydneylance
"""

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
all_lowercase_letters = string.ascii_lowercase
all_uppercase_letters = all_lowercase_letters.upper()
all_letters = all_lowercase_letters + all_uppercase_letters



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if (char in str(letters_guessed)) == False:
            guess = False
            break
        else: 
            guess = True
    return guess


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    store_correct_letters = [] #stores correct letters
    guessed_string = "" #string output
    for i in letters_guessed:
        if i in secret_word:
            store_correct_letters.append(i) #add correct letters to list
    
    #adds letters and blanks to string
    for char in secret_word:
        if char in store_correct_letters:
            guessed_string += char + " "
        else:
            guessed_string += "_ "
            
    return guessed_string



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = "" #string of letters not guessed
    all_lowercase_letters = string.ascii_lowercase  #string of all lowercase letters
    
    for char in all_lowercase_letters :
        if char not in letters_guessed:
            letters_not_guessed +=  char
    
    return letters_not_guessed


def secret_word_letter_count(secret_word):
    ''' 
    secret_word: string, the word the user is guessing
    Returns: number of letters in the secret word
    '''
    count = 0
    for i in secret_word:
        count += 1
    return count

def unique_letters_secret_word(secret_word):
    ''' 
    secret_word: string, the word the user is guessing
    Returns: number of unique letters in the secret word
    '''
    all_lowercase_letters = string.ascii_lowercase
    all_uppercase_letters = all_lowercase_letters.upper()
    all_letters = list(all_lowercase_letters + all_uppercase_letters)
    
    letters_used = []
    unique_letter_count = 0
    
    
    for char in all_letters:
        if char  in secret_word:
           all_letters.remove(char)
    for i in secret_word:
        if i not in all_letters:
            unique_letter_count += 1 
        else:
           unique_letter_count -= 1 
    return unique_letter_count


def guess_is_vowel(most_recent_guess):
    ''' vowels: string, list of vowels
    most_recent_guess: user input, guess
    Returns: True if user guess is a vowel, False if consonant
    '''
    vowels = "aAeEiIoOuU"
    if most_recent_guess in vowels:
        return True
    else:
        return False
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #defining variables
    num_guesses_remaining = 6 # number of guesses allowed to use in loop
    num_warnings_remaining = 3
    total_guesses_allowed = 6 #number of guesses allowed
    letters_guessed = [] #storing letters guessed
    
        
    print("Welcome to the glorious game of Hangman! I am thinking of a word that is", secret_word_letter_count(secret_word), "letters long. You will get", total_guesses_allowed, "guesses. Make sure all guesses are lowercase and please do not guess more than one letter per round.")
    
    while num_guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False :
        most_recent_guess = input("Please guess a letter:") #user inputs guess
        most_recent_guess = most_recent_guess.lower() #changes guess to lowercase
        if (most_recent_guess in get_available_letters(letters_guessed)): #if user input is in characters avaiable to guess from 
                letters_guessed.append(most_recent_guess) #adding guess to list
                if (guess_is_vowel(most_recent_guess) == False) and (most_recent_guess not in secret_word):
                    num_guesses_remaining -= 1 #subtracting guess from total guess count
                elif (guess_is_vowel(most_recent_guess) == True) and (most_recent_guess not in secret_word):
                    num_guesses_remaining -= 2 #subtracting guess from total guess count
                
                #output from loop: remaining guess count and hangman letters guessed along with blanks as "_"
                
                print(get_guessed_word(secret_word, letters_guessed))
                print("Guesses remaining:", num_guesses_remaining)
                print("Available letters:", get_available_letters(letters_guessed))
                
        elif (most_recent_guess not in all_lowercase_letters) and (most_recent_guess not in all_uppercase_letters): # output condition if character not allowed
            num_warnings_remaining -= 1
            print("This character is not allowed (dummy). You have", num_warnings_remaining, "warnings remaining. Please guess again")
            
        elif most_recent_guess not in get_available_letters(letters_guessed): #output condition if 
            num_warnings_remaining -= 1
            print("This character was already guessed (dummy). You have", num_warnings_remaining, "warnings remaining. Please guess again.")
            
        if num_warnings_remaining == 0:
            num_guesses_remaining -= 1
            
    if is_word_guessed(secret_word, letters_guessed) == True: # output when secret word is guessed
        print("You guessed the secret word! Congrats, you're a genius!")
        total_score = num_guesses_remaining * unique_letters_secret_word(secret_word)
        print("Your total score is:", total_score)
        
    if num_guesses_remaining <= 0 : #output if user didn't guess correcty in alotted number of guesses
        print("You didn't guess the word in", total_guesses_allowed, "guesses (dingleberry). The secret word was", " '' " + secret_word + ".''")
        
    
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
   
    num = 0
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if (my_word[i] == '_') or (my_word[i] == other_word[i]):
                num += 0
            else:
                num += 1
        if num == 0:
            return True
        else:
            return False
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    hint_list = []

    for word in wordlist :
        if match_with_gaps(my_word, word) == True :
            hint_list.append(word)        
    return hint_list



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    

  #defining variables
    num_guesses_remaining = 6 # number of guesses allowed to use in loop
    num_warnings_remaining = 3
    total_guesses_allowed = 6 #number of guesses allowed
    letters_guessed = [] #storing letters guessed
    
        
    print("Welcome to the glorious game of Hangman! I am thinking of a word that is", secret_word_letter_count(secret_word), "letters long. You will get", total_guesses_allowed, "guesses. Make sure all guesses are lowercase and please do not guess more than one letter per round.")
    
    while num_guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False :
        most_recent_guess = input("Please guess a letter:") #user inputs guess
        most_recent_guess = most_recent_guess.lower() #changes guess to lowercase
        if (most_recent_guess in get_available_letters(letters_guessed)): #if user input is in characters avaiable to guess from 
                letters_guessed.append(most_recent_guess) #adding guess to list
                if (guess_is_vowel(most_recent_guess) == False) and (most_recent_guess not in secret_word):
                    num_guesses_remaining -= 1 #subtracting guess from total guess count
                elif (guess_is_vowel(most_recent_guess) == True) and (most_recent_guess not in secret_word):
                    num_guesses_remaining -= 2 #subtracting guess from total guess count
                
                #output from loop: remaining guess count and hangman letters guessed along with blanks as "_"
                
                print(get_guessed_word(secret_word, letters_guessed))
                print("Guesses remaining:", num_guesses_remaining)
                print("Available letters:", get_available_letters(letters_guessed))
                
        elif (most_recent_guess not in all_letters) and (most_recent_guess != "*") : # output condition if character not allowed
            num_warnings_remaining -= 1
            print("This character is not allowed (dummy). You have", num_warnings_remaining, "warnings remaining. Please guess again")
            
        elif most_recent_guess not in get_available_letters(letters_guessed) and (most_recent_guess != "*"): #output condition if the letter was already guessed
            num_warnings_remaining -= 1
            print("This character was already guessed (dummy). You have", num_warnings_remaining, "warnings remaining. Please guess again.")
        
        elif most_recent_guess == "*":
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            
        if num_warnings_remaining == 0:
            num_guesses_remaining -= 1
            
    if is_word_guessed(secret_word, letters_guessed) == True: # output when secret word is guessed
        print("You guessed the secret word! Congrats, you're a genius!")
        total_score = num_guesses_remaining * unique_letters_secret_word(secret_word)
        print("Your total score is:", total_score)
        
    if num_guesses_remaining <= 0 : #output if user didn't guess correcty in alotted number of guesses
        print("You didn't guess the word in", total_guesses_allowed, "guesses (dingleberry). The secret word was", " '' " + secret_word + ".''")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#      pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
