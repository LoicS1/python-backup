from __future__ import print_function
import random
import time
    
def celeb_game():
    '''
    '''
    secret = "donald trump"
    lives = 5
    dis_word = ""
    while lives > 0:
        guess = str(raw_input("Guess a letter: "))
        for char in secret:
            if char in guess:
                dis_word += char
            elif char == " ":
                dis_word += " "
            else:
                dis_word += "_"
        print (dis_word)
        lives -= 1
        print (lives)
        if dis_word == secret:
            print ("You have guessed the word!")
        #return (lives) #don't change anything it kind of almost works


    
def hangman():
    ''' 
    '''
    celeb_list = ["donald trump", "kim kardashian", "stephen curry", "bill gates",
    "tom brady", "kanye west", "steve jobs", "beyonce", "adam brown", "justin bieber",
    "oprah", "michael jackson", "michael jordan", "lebron james", "eminem", ""]
    print ("Welcome to Celebrity Hangman!")
    time.sleep(1)
    celeb_game()
    
    
    
def hangman_display(guess, secret):
    '''The function is checking if the characters in secret match with the 
    letters guessed by the user. If the character matches with the guess it will
    store the character a new variable dis_word. If the character of the secret
    is ever a space it will add a space into the dis_word variable. Lastly, if
    the character does not match any in guess it adds an underscore in place of
    the missing characters.'''
    dis_word = ""
    for char in secret:
        if char in guess:
            dis_word += char
        elif char == " ":
            dis_word += " "
        else:
            dis_word += "_"
    print dis_word #returns the letters that match the secret word to the user, as 
    # as well as any spaces in the secret word, and underscores for letters in the 
    # secret word not guessed yet.


    
    
    
    
# things to add on:  hints, ability to guess one letter at a time, or a whole word, if you fail, prints secret, give more difficult words as time 
# goes on 

# for reference

from __future__ import print_function
import random
import time

def hangman_display(guess, secret):
    '''The function is checking if the characters in secret match with the 
    letters guessed by the user. If the character matches with the guess it will
    store the character a new variable dis_word. If the character of the secret
    is ever a space it will add a space into the dis_word variable. Lastly, if
    the character does not match any in guess it adds an underscore in place of
    the missing characters.'''
    dis_word = ""
    for char in secret:
        if char in guess:
            dis_word += char
        elif char == " ":
            dis_word += " "
        else:
            dis_word += "_"
    print (dis_word) 
    if dis_word == secret:
        print ("You have guessed the word!")
    #returns the letters that match the secret word to the user, as 
    # as well as any spaces in the secret word, and underscores for letters in the 
    # secret word not guessed yet.


    
def hangman():
    ''' 
    '''
    celeb_list = ["donald trump", "kim kardashian", "stephen curry", "bill gates",
    "tom brady", "kanye west", "steve jobs", "beyonce", "adam brown", "justin bieber",
    "oprah", "michael jackson", "michael jordan", "lebron james", "eminem", ""]
    print ("Welcome to Celebrity Hangman!")
    time.sleep(1)
    lives = 5
    secret = random.choice(celeb_list)
    print (secret)  
    time.sleep(1)
    print ("You have " + str(lives) + " lives in this game.")
    #guesses = ''
    char_bank = '' #need to work on this 
    while lives > 0:
        guess = raw_input("Guess: ")
        hangman_display(guess, secret)
        #if guess in secret:
            #print (hangman_display(guess, secret))
        if guess == secret:
            break
        #if len(guess) > len(secret):
            #print ("You've been caught cheating!")
            #break
        lives -= 1
        print ("You have " + str(lives) + " lives left")
    if lives == 0:
        print ("You have ran out of lives! The secret word is: " + secret)