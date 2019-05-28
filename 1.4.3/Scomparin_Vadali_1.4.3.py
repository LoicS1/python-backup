from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations


#4.

# Arrays and lists both contain data, and both allow for easy access later on.
# Arrays are multidimensional, whereas lists are only a single dimension of values.

#5.
"""
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
# Saves the figure
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow
fig.savefig('women2')
"""

#5. 

'''
the image height = the number of rows of pixels = 960
	the image width = the number of columns = 584
	the green intensity at (5,9) = img[5][9][1]
the red intensity at (4,10) = 62
	the red intensity of the 25th pixel in the 50th row = 79
'''
"""
#6.

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
# Saves the figure
###
# Make a rectangle of pixels green
###

height = len(img)
width = len(img[0])
for row in range(424, 467):
    for column in range(136, 160):
        img[row][column] = [0, 255, 0] # green
fig.savefig('green_earing.png')
"""

#7.
"""
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
# Saves the figure
###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
###
# a.
# The program looks at all the pixels in the top 155 rows and across all colums,
# and if their RGB value is greater than 500 (high brightness), then the program
# assumes that those pixels represent the sky and colors them magenta. The [r] and
# [c] represent the rows and columns within the array of pixels.

#b

height = len(img)
width = len(img[0])
for r in range(422, 467):
    for c in range(135, 162):
        if sum(img[r][c])>400: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
fig.savefig('women_sky_earing.png')
"""

#8.


import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(0, 100, 3):
        for column in range(0, 100, 3):
            if (row+column) < 130 or (row+column) > 150: #(row+column)/stripe_width % 4 == 0: #and (row+column) < 100: 
                if (row+column)/stripe_width % 3 == 0 or (row+column)/stripe_width % 3 == 1:
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                    image[row][column] = [255, 255, 0, 255] # magenta, alpha=255
            
            elif 130 <= (row+column) <= 150:
                for row in range(60, 80, 2):
                     for column in range(60, 80, 2):
                        image[row][column] = [255, 255, 0, 255] # magenta, alpha=255
            
            
            else:
                # Odd stripe
                image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask7')       
    
    
# 9.

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'women_sky_earing.png')
filename_1 = os.path.join(directory, 'mask7.png')
# Read the image data into an array
img = plt.imread(filename)
img_1 = plt.imread(filename_1)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img_1, interpolation = 'none')
# Show the figure on the screen
fig.show()
fig.savefig('woman_mask')
