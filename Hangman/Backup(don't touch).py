from __future__ import print_function
import random
import time 

def hangman_display(guess, secret):
    '''The function is checking if the characters in chosen secret word (the 
    second parameter) match with the letter guessed by the user (the first 
    parameter). If the character matches with the guess it will
    store the character in a new variable called dis_word. If the character of the secret
    is ever a space it will add a space into the dis_word variable. Lastly, if
    the character in guess does not match any in the secret word it adds an 
    underscore in place of the missing character. Since the function is called by
    the hangman() function, no arguments are directly entered by the user in this
    function.'''
    dis_word = ""
    for char in secret:
        if char in guess:
            dis_word += char #stores the correctly guessed letters in a new variable
        elif char == " ":
            dis_word += " " #stores any spaces found in a new variable
        else:
            dis_word += "_" #stores any non correctly guessed letters found as underscores in a new variable
    return dis_word
    #returns the letters that match the secret word to the user, as 
    # as well as any spaces in the secret word, and underscores for letters in the 
    # secret word not guessed yet.

def play_again():
    '''
    Asks and accepts yes/no reponses from the user regarding whether they want to play
    another round of Hangman or exit the game. If they want to play, the hangman()
    function is called again.
    '''
    new_round = raw_input("Would you like to play again, yes or no?: ")
    if new_round == "yes":
        hangman() #calls Hangman function to play again
    elif new_round == "no":
        print ("Thanks for playing and see you later!")
    else: #in case the user types something in wrong
        print ("enter either yes or no as an answer")
        time.sleep(2)
        play_again()
    
def hangman():
    ''' 
    This function iniates the hangman game and selects a random celebrity name from
    a list of names. It then tells the user the rules of the game and how many lives
    the user has. A while statement then allows the user to play by guessing a character 
    and then calling the hangman_display function as long enough lives remain.  
    After each execution of the hangman diplay function, this function checks:
        if user has cheated by guessing more than one character at a time, in which 
        case the game is terminated
        if the cumulative list of characters entered in the guesses matches the secret
        word, in which case the user wins and the game is over
        if the character guessed is present, in which case all the guessed characters
        and blanks left are printed
        if the character guessed is not present, in which case all the guessed characters
        and blanks left are printed, and a statement is printed saying the user lost a life
        if the user ran out of lives, in which case the game is terminated.
    If the game is over for any reason, another function is called asking the user
    if they want to play again or not.
    '''
    
    celeb_list = ["donald trump", "kim kardashian", "stephen curry", "bill gates",
    "tom brady", "kanye west", "steve jobs", "beyonce", "adam brown", "justin bieber",
    "oprah", "michael jackson", "michael jordan", "lebron james", "eminem"]
    print ("Welcome to Celebrity Hangman!")
    time.sleep(1)
    print ("You will be prompted to guess the name of a famous person. Please guess only one lowercase letter at a time.")
    time.sleep(2)
    lives = 7
    secret = random.choice(celeb_list) #selects a Celebrity name from the list
    print (secret)  #used only for testing of game
    time.sleep(1)
    print ("You have " + str(lives) + " lives in this game.")
    char_bank = '' #variable that will contain all the correctly guessed letters
    
    while lives > 0:
        guess = raw_input("Guess: ") #lets the user guess a character
        char_bank += guess
        
        if len(guess) > 1:
            print ("Are you trying to cheat?! Guess only one letter next time!")
            break #exits while loop if user guesses more than one word, therefore ending game
     
        if hangman_display(char_bank, secret) == secret:
            print (hangman_display(char_bank, secret)) #checks of letters in the bank match those
            # in the secret word
            time.sleep(1)
            print ("Congrats! You have guessed the secret person!")
            break
        
        if guess in secret:
            print (hangman_display(char_bank, secret)) #lets the user know where the letter
            # they guessed correctly is
        else:
            print (hangman_display(char_bank, secret)) #lets the user that they
            # didn't guess a letter in the word and lost a life
            lives -= 1
            print ("Oops, wrong letter! You have " + str(lives) + " lives left.")
       

        if lives == 0: #ends game and lets user know they ran out of lives
            print ("You have ran out of lives! The secret word is: " + secret)
    
    play_again()
    
hangman()