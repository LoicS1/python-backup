from __future__ import print_function # use Python 3.0 printing 



def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
    
def report_grade(percent):  
    '''Show mastery based on percent'''
    GRADE_LIMIT = 80
    if percent < GRADE_LIMIT:
        print('A grade of', percent, '''does not indicate mastery. Seek extra 
        practice or help''')
    else:
        print('A grade of', percent, '''indicates mastery. Keep up the good 
        work!''')
        
    
def letter_in_word(guess, word):
    '''shows if letter is in word'''
    if guess in word:
        return True
    else:
        return False
        
def hint(color, secret):
    secret = ['red','red','yellow','yellow','black']
    if color in secret:
        print("The color " + str(color) +  " IS in the secret sequence of colors.")
    else:
        print ("The color " + str(color) + " is not in the secret sequence of colors.")
        #actually don't need str since print function already imported at top, just use commas

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

    