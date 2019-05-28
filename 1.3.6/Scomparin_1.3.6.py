#4. (5,7,6) An example of a tuple

#5. This assigment needs to be completed with answers written as comments in the 
# program file.
# Variable names are to be lowercase and not contain spaces.

#6. Tuples

#6a. some_values[1] will return b because b has index 1 within the tuple.
#6b. some_values[0:2] will return a and b because those have indices of 0 and 1
# within the tuple.

#7a. b[1] returns True because b[1] is a which is equal to 10.
#7b. Since b was already defined using a, b[1] is still 10.

#8. values[1:] returns ['b', 3] because b has index 1 and 3 has an index greater 
# than 1 (2).

#9. values[2] is assigned to '3', which is a string. Therefore, it is not 
# assigned to 3, a number.

#10a. 4 and 5 were added to the list of values, so there are now 5 values in the 
# list. This was able to be done because [4,5] is already a list.
#10b. [6, 7] is considered a list, and was simply appended- added to the 
# end of the values list. A list can be placed within a list.

#11. 5 is an int, not a list, and only a the items in a list can be added to 
# another list.

#12. a was multuplied by 3 and the product (18) assigned to a.

#13
import random

#14.
def roll_two_dice():
    a = random.randint(1,6);
    b = random.randint(1,6);
    return a + b
   
    

#Conclusion

#1. a is a string, b is a tuple, and c is a list.
#2. Integers cannot be assingned new values to model new situations- they are 
# merely constant values.
#3. There are different ways to store, rewrite, and extract data in python. This
# includes the use of variables to that can be assigned different data values, as
# well as functions that transform a particular input into an output. List and tuples
# can be used to store data, and lists are modifiable. All of these properties of 
# Python allow the programmer to build upon different actions and reuse key data
# within their project.

#1.3.6 Function Test
print(roll_two_dice())

#The result was the sum of two dice, and was random, ranging from 2 to 12. Since that
# matches the intention of the function, the assignment has been completed correctly.