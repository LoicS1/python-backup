'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')

print(earth_img.size)
print(earth_small.size)
print(earth_img.size[1])


#13.
"""
matplotlib.pyplot (plt) The matplotlib library helps to plot images on a coordinate plane.

numpy (np) Creates an array set for the images.

PIL  manipulates the images by cropping, filtering, etc
"""

#15.

'''
a.
Line 19 calls the function subplots from the matplotlib library. The function is being
called with 2 argument(s): 1,2. The function returns 2 object(s), which is/are being assigned to ax.

b.
Line 20 calls __imshow()_ on ___ax[0]____
Line 23 calls __imshow()_ on ___ax[1]____
Line 24 calls __set_xticks_ on ___ax[1]____
Line 25 calls __set_xlim_ on ___ax[1]____
Line 26 calls __set_ylim_ on ___ax[1]____
Line 27 calls __savefig_ on ___fig____

c.
1162, 966

'''

#16.
'''
#a width: 13.125 px
height: 13.125 px
top left: (202.875, 237.75)
bottom right: (216, 250.875)
'''

#17.
'''
a. Line 30 uses the join() method from the os.path module. It is being passed 2 arguments. The value it returns is being assigned to the variable earth_file.
b. In line 31 the open() function of the PIL.Image module returns a new PIL.Image object, which is being assigned to the variable earth_img. 
c. In line 32 the resize() method takes only one argument: a 2-tuple. Explain why there are two sets of parentheses in this line. The inner coordinates represent the coordinate pair reprsenting the height and width of the image.
d. The (89, 87) specifies the number of rows and columns of pixels the resized image will have.
e. Line 33 calls the function subplots from the plt library with 2 argument(s): 1, 2. The function returns 1 object(s), which is/are being assigned to axes2.
Line 34 calls the method imshow on the object axes2[0] with _1 argument(s): earth_img. 
Line 35 calls the method imshow on the object axes2[1] with _1 argument(s): earth_small. 
Line 36 calls the function savefig from the PIL library with 1 argument(s): 'resize_earth'. The function returns 1 object(s), which is/are being assigned to fig2.
f. i)Resize also contains an optional resample parameter
ii) The default value is nearest
iii) PIL.Image.LANCZOS is recommended to downsample the image.
g. The width an height of the new image in order for the old image to be compressed.
h. this prints the number of rows in both images and the number of columns in the first image.
i. the values on the matplot axis are less on the second image than on the first image
'''
'''
18. resize anazyles the rgb values of a group of pixels (say 3 by 3) and decides a best color for the new pixel in the resized image based on those values. This 
procedure is repeated for all adjacent pixels until the best color combination is determined

19. 

#a 
"""
student_img: The size is 1920 * 2720 * 3 = 15, 667, 200
earth_small: The size is 89   * 87   * 3 = 23, 229
"""

#b
earth_small.save('smallEarth.png')

#c
"""
smallEarth = 87.5 * 85.5 * 100
smallEarth: 748,125
student = 1920 * 2720 * 3
student: 15,667,200
"""
#d
"""
In step a, the values have increased due to the resizing of the images. This is 
changes the values since the image size is different.
"""
#e 
"""
In the paste method, if you add a color, it will set all the pixels to the color
that you want. This will set multiple pixels to the same color, if you add a 
color parameter. 
"""
#f
"""
According to the documentation, the code omitted, a mode is chosen so that all 
information in the image and the palette can be represented without a palette. 
When converting from a colour image to black and white, the library uses the 
ITU-R 601-2 luma transform: L = R * 299/1000 + G * 587/1000 + B * 114/1000. When
converting to a bilevel image (mode1), the source image is first converted to
black and white.
"""
#g
"""
The aurguments are explaining the file of which you want to paste on the old 
image. You also need to explain the location of where you want to add the images.
And finally, the mask is to take the area you are currently in. 

"""
'''
#20 
# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966) ,mask=earth_small) 
student_img.paste(earth_small, (708,944), mask = earth_small)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_as_eyes')












































