#5. We could use int or float because those are the two types that represent 
# numbers

#6. Ipython says that since there are not quotes around the 5, it is an int, not
# a string, and therefore cannot be concatenated with a string

#7. slogan[-7] is h because h is the 7th to last character in the predefined string.

#8. Slicing
# slogan[5:21] outputs 'hool is the best'
# slogan[:5] returns 'My sc'
# slogan[17:21] returns 'best'

#9. slogan[3:13] + 'cool' = 'school is cool'

#10a. len(activity) is 7 since activity has 8 letters (they have index values
# of 0-7)

#10b. activity[0 : len(activity)-1] is 'theate' because index 0 is t and the last
# index, r, is removed because of the (activity)-1

#11. 'Goo' is part of the string 'Greatest good for the greatest number!', so the
# boolean returns true

#12.

def how_eligible(essay):
    '''tests whether a written piece can be entered in a contest'''
    count = 0
    if '?' in essay:
        count += 1
    if ',' in essay:
        count += 1    
    if '!' in essay:
        count += 1 
    if '"' in essay:
        count += 1 
    print count
    
# Assignment Check #1

#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

# The first sentence, based on the function I built, satisfied all 4 requirements,
# and the second only satisfied one. Based on this result, I have successfully 
# completed the assignment.