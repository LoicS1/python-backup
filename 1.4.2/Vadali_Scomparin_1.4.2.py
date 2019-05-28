

#7.

 #shows DISPLAY error
"""JDoe_JSmith_1_4_2: Read and show an image."""

import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
"""
''''''Read the image data''''''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

''''''Show the image data''''''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
"""


'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
"""
import matplotlib 
matplotlib.use('Agg') #makes it usable in a non-GUI environment
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show() #used for a GUI backend 
fig.savefig('women_plot')
"""
# Explanation
'''matplotlib.use(Agg) changes the environment to make it a non-graphical user interface, 
which allows the image to be properly displayed in Clould9, which is a non GUI environment. If
this statement is left out, the imported environment remains GUI, causing errors in the Cloud0
interface.'''

#a. The coordinate pair for the woman's nose is (260, 410).

#b.

'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
"""
import matplotlib 
matplotlib.use('Agg') #makes it non-GUI
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
'''directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

''''''Show the image data''''''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_plot.png') #saves the entire figure (not just the image) as a file called 'cat_plot.png'.'''
"""
#The tip of the cat's nose is at (470, 246)

#8.

#a
#fig is an instance in the class figure. The figure is the entire saved file, not 
# just the image in contains.

#ax is an instance of the class AxesSubplot. ax shows the horizontal and vertical 
# coordinates of the image within the figure.

#b
#In line 25, the method savefig is being called on the object fig. That method is being given 
# 1 arguments. That method is a method of the class figure. 

#c see added comments above.

#9.


# a. the method imshow is being executed on the object ax[0]

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#bi)

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)


'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('tow_woman.png')

#ii)
"""
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)


'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats.png')


'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#10 

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')
"""

'''the interpolation argument can be used to set the interpolation on or off within the 
imshow function, since c9 is a non-gui interface. The "lim" part of the code allows c9
to crop the image to show just the earing.
'''

# 11a)
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[0].minorticks_on()
ax[0].set_xlabel("this is the x label")
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
ax[1].set_title("This is my first image in Python!")
ax[1].set_ylabel("Height of the earing")
# Show the figure on the screen
fig.show()
fig.savefig('experiment.png')
"""

#11b.
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[2].imshow(img)
ax[0].set_xlim(140, 150)
ax[0].set_ylim(450, 440)
ax[1].set_xlim(155, 165)
ax[1].set_ylim(430, 420)
ax[2].set_xlim(145, 155)
ax[2].set_ylim(470, 460)
# Show the figure on the screen
fig.show()
fig.savefig('three_closeup.png')
"""
#12.

# The method ax.fill takes the arguments: sequence of x, y, [color]. The x and y
# values tell the computer from which coordinates to draw the lines of a polygon
#from and to, so that the interior of the polygon is closed and defined within
# the program. The color parameter can take a one string letter argument describing a 
# color, such as "b" for blue. x and y have to be defined but the color can be selected
# randomly from the library if not entered.

#13.
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[1].plot(39, 48, 'ro')
ax[1].plot(118, 42, 'ro')
ax[1].plot(141, 41, 'ro')
# Show the figure on the screen
fig.show()
fig.savefig('crazy_mice.png')
"""

# Conclusion

#1.

'''Absolute and relative filenames are both ways to access a file within different
directories. An absolute filename begins at the root directory and then passes through 
child directories until the file is reached. A relative filenames begins in a child directory
of the root directory and only passes through child directories of that directory.
'''

#2.

'''
An object is an instance of a class, to which methods of that class and its parent 
classes can be applied to.
'''

#3.

'''
A method is a function that can be applied to an object of a class. Properties on 
an object are its characteristics such as any values it contains or type, such as string
or int.
'''

#4.

'''
When a method is called on an object, the object is modified in some way, and can
be renamed as a new object, such as the image files we saved in this exercise. 
'''