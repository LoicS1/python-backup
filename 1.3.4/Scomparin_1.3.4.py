'''Part I. Nested if structures and testing'''

from __future__ import print_function # must be first in file 
import random

#1.
def food_id(food):
    ''' Returns categorization of food
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
# 1a. 'NOT Citrus, Fruit'. The code on line 17 was executed.
# 1bi. the input 'orange' will cause this line to be activated
# bii. any of the items in the fruit list will return this
# biii. a starchy food (banana or potato) will cause this
# biv. a food item not listed at all above will cause this
# c. Since banana is already part of the "fruits" list, the else block will
# not be ran at all

#2.
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
#3. 
def f(n):
    '''test to determine whether a number is a multiple of 6, even, odd, and/or
    an integer'''
    if int(n)==n:
        if n%2 == 0:
            if n%3 == 0:
                print('the number is a multiple of 6')
                return '6'
            else:
                print('n is even')
                return 'even'
        else:
            print('n is odd')
            return 'odd'
    else:
        print('N is not an integer')
        return 'float'
        
        
#4. 
#To test all the different parts of the function, we could test a float
# which would not be an integer. Then, we would test an odd number, then an even 
# number that is not a multiple of six, and finally a number that is a multiple of 
# 6. All of these numbers would be compared to the float, odd, even, and 6 that 
# would be returned from the function to see whether the inputted numbers match 
# these expected return values.
        
        
#5.
def f_test():
    ''' unit test for f(n). returns True if good, returns False and 
    prints error if the chosen number does not match the return value it is 
    supposed to
    '''
    works = True
    if f(6) != '6':
        works = 'multof 6 bug'
    if f(4.5) != 'float':
        works = 'int bug'
    if f(3) != 'odd':
        works = 'odd bug'
    if f(8) != 'even':
        works = 'even bug'
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
#Part 2
        
# 7. Concatenation involves adding strings together (that is what the + is used for).
# + as numeric addition add two numbers (type float or int) together.

#8.
#a. Line 11 also has two arguments and a key-value pair. The "end" keyword allows
#the ! to be added to the end of the previous phrase. The space between the 
# string and guess allow for a space betweeen the phrase and the guess number.
#b.
def guess_once():
    ''' picks a random number between one and 4 and compares it to user's guess
    '''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess > secret:
        print('Too high, my number was ', secret, '!', sep='')
    elif guess < secret:
        print('Too low- my number was ', secret, '!', sep='')
    else:
        print('Right on, I was number', guess, end='!\n')
        
#9
def quiz_decimal(low, high):
    '''tell the user whether a number they picked in between a high and low value
    they also chose
    '''
    print('type a number between', low, 'and', high)
    guess = float(raw_input('Number: '))
    if low < guess < high:
        print("Good!", low, "<", guess, "<", high)
    elif guess < low:
        print("No,", guess, "is less than", low)
    else:
        print("No,", guess, "is greater than", high)
    
#Conclusion

#1. Glass-box testing runs through the if-else structure of the function that 
# needs to be tested. That was, the programmer knows whether the if/else condition
# produces the desired output (such as a string saying something).

#2. The highest amount of blocks that could be executed are all the if blocks
#, plus the innermost else block. This would happen if the argument satisfies every
# condition except the very last one. However, only two blocks could be executed 
# if the argument fails to satisfy the first condition. Therefore, the amount of 
# blocks executed varies.

#3. A test suites runs through all the if-else statements for the function that 
# is being tested to verify whether the output the programmer intended for each condition
# matches what is actually produced. By designing the test suite first, programmers
# can proactively identify and reduce errors when they design the actual function's
# code, which helps them save time. They also have a better vision of what specific
# goal to tailor their code to.

#4. functions for each output case:

def int_f(n):
    '''tests whether n is an integer
    '''
    if int(n)==n:
        print('n is an integer')
    else:
        print('n is not an integer')
    
def even_f(n):
    '''tests whether n is even or not
    '''
    if n%2 == 0:
        print('n is even')
    else:
        print('n is not even')
  
def odd_f(n):
    '''tests whether n is odd or not
    '''
    if n%2 != 0:
        print('n is odd')
    else:
        print('n is not odd')
        
def divisible_by_6_f(n):
    '''tests whether n is divisible by 6
    '''
    if n%6 == 0:
        print('n is divisible by 6')
    else:
        print('n is not divisible by 6')

#Challenge
#1.

def f_challenge(n):
    '''determines how well the 4 functions defined above work together'''
    int_f(n)
    even_f(n)
    odd_f(n)
    divisible_by_6_f(n)
    
#Assignment Check #1

#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)

# Based on the results of the code, I believe I have completed the assignment 
# sucessfully because all the functions returned the values that were expected 
# based on the given fruit or number argument.
    
        
    