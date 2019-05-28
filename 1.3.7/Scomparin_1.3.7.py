# %run 1.3.7/file.py
# cd 1.3.7, %run file.py will not work unless remove 1.3.7 for the histogram in given code
from __future__ import print_function
import random

#4.
def days():
    ''' Prints the days of the week and then, for days 5-7, prints it is that day of September.
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
#5. 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def picks():
    '''
    Makes a bell curve graph showing how frequently what numbers are randomly chosen out of
    a set containing 1, 3, 6, and 10.
    '''
    a = [] # an empty list
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])] #change the choices to make a bell curve
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')

#6a.
def roll_hundred_pair():
    '''
    Rolls 2 dice 100 times and produces a histogram showing how common each sum of
    the results of the two dice (from 2-12) is.
    '''
    a = []
    a += [random.choice([1, 2, 3, 4, 5, 6])]
    for choices in range(100):
        a += [random.choice([1, 2, 3, 4, 5, 6])]
    plt.hist(a)
    plt.savefig('1.3.7/picks')
    
#6b. 
def dice(n):
    '''
    Randomly rolls a number of dice the user specifies as an argument and returns
    the sum of the values of the rolled dice.
    '''
    total = 0

    for x in range(0,n):
        total += random.randint(1,6)
    
    print('Roll was ' + str(total))
      
      
#7.
def validate():
    '''
    Prompts the user with a string and asks them to enter a character present in
    the string until they do so, after which the function gives them a printed 
    thank you statment. If the user does not guess an applicable letter, they 
    must keep guessing, as a while loop wihtin the function keeps running.
    '''
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
     
# Line 2 is necessary because guess needs to be initialized before being used in the while loop. 
        
        
#8.

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    Prompts the user to guess which person won the lottery by iterating through a list
    of names, which is entered as an argument, and printing each one, and then prints how many
    guesses the user took to guess the right person. The number of guesses, an integer,
    is increased through a while loop as long as the user guesses wrong, and exits the while
    loop if the user guesses right.
    '''
    winner = random.choice(players) 

    ####
    # Prints the question statement, including the players's names, by using a for 
    # loop to iterate through the list of the player's names.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # iterates through each player by index 
    # the length of the list is 4 players, and the last player has index 3, so 
    # that is where the -1 comes from
        print(p+', ', end='')
    print(players[len(players)-1]) # Prints all 4 players (indices 0-3) in the list of players 
    # seperated by commas (the p + ', ' is concactenation)
    # so that the user can see the names and choose one.

    ####
    # The number of guesses is initialized at 1. The raw_input function asks the user to 
    # enter a person's name, and if not equal to the person the computer selected
    # randonmly, the while loop is activated and tells the user to guess again. If 
    # the condition for the while loop is not mentioned (the user guesses right),
    # the print statement outside the while loop tells the user how many guesses they
    # took to guess right.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
    
#9.

def goguess():
    '''
    Chooses a number from 1 to 20 and asks the user what number has been chosen until the
    user guesses correctly. Once the user guesses correctly, the function prints
    how many guesses it took the user to guess correctly.
    '''
    number = random.randint(1,20)
    print ("I have a number between 1 and 20 inclusive.")
    guess = int(raw_input("Enter an integer from 1 to 20: "))
    guess_count = 1
    while guess != number:
        print
        if guess > number:
            print(guess, "is too high")
            guess = int(raw_input("Enter an integer from 1 to 20: "))
            guess_count += 1
        elif guess < number:
            print(guess, "is too low")
            guess = int(raw_input("Enter an integer from 1 to 20: "))
            guess_count += 1
            
    print ("Right! My number is " + str(number) + "! You guessed in " + str(guess_count) + " guesses!")
        
    
    
        
#10.
# This cannot be determined because it depends on the original guess. If the original guess
# is around 3000, then half the options will be eliminated because the user will know to
# guess either higher or lower.

#11a.

def matches(ticket, winners):
    '''
    Compares two lists of numbers entered as arguments by the user and returns the
    number of values present in both lists.
    '''
    common = 0
    for int in ticket:
        if int in winners:
            common += 1
    print (common)
    
#11b.

def report(guess, secret):
    '''
    Asks the user to guess a list of words as an argument and compares how many of the words the 
    user inputted match words, and their indices on a secret list that the user also 
    enters as an argument. This function also compares which words match regardless
    of their indices in both lists. The number of words that match these two qualities 
    is display as a list in the form [word-index matches, word matches with different indices]
    '''
    counter = 0
    in_secret = 0
    not_in_secret = 0
    for word in guess:
        if word in secret:
            if guess[counter] == secret[counter]:
                in_secret += 1
            else:
                not_in_secret += 1
        counter += 1
    answer = [in_secret, not_in_secret]
    print (answer)
    
#Conclusion

#1. Developing a program this way is more time-consuming and prone to syntax errors 
# that the user makes on accident. Also, if there needs to be a change in the code, then the 
# change needs to be made in all lines of code that is repeated rather than just one
# loop. Finally, the program will run slower as more lines of code needs to be executed.

#2. Iteration is the process by which a large set of data is anayzled. One key method to
# analyze data is to iterate through each value of a list and search for a particular
# quality. In short, this produces more data that can then be anazyled by conventional methods
# such as a graph, because the values that meet the criteria have been isolated by the interation.

#3. A for loop executes again for each iterable element in a list and then stops once it 
#reaches the end of the list. A while loop is executed as long as a certain condition is met.
# While loops are more used to do something only if a certain value is reached or a statement is true
# or false. While loops also have the potential to become infinite loops if they
# conditions they require are always sastisfied.

#4. Samraat and I worked well to try to decipher some of the tougher functions. We
# both worked on different parts of the function at the same time in order to be more
# efficient, or one person guided the other who has programming. I think our style
# is efficient and embodies pair programming, but we should work on these assingments
# more in advance so we can come prepared to class with more questions, since we had some
# trobule with some of the functions.
            
# Assignment Check:
days()
picks()
roll_hundred_pair()
dice(3)
validate()
guess_winner()
goguess()
ticket = [11, 12, 13, 14, 15]
winners = [3, 8, 12, 13, 17]
matches(ticket, winners)
guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
report(guess, secret)

# Based on the results of the assingment check, all the functions seem to work correctly
# except for #11b. I was having trouble finding a way to compare the word at an index
# in the guess list to all the words in the secret list with the same index or higher.


#Qualities of a good docstring- for reference

#1. what arguments needs to be entered based on the parameters
#2. what this function does with those arguments
#3. what it returns/outputs.