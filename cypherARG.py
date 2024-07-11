## Author: Rodolfo Perez
## Date: 07/10/2024
## Last modified: 07/10/2024

## Usage: compile the code py.exe .\cypherARG.py to encode a text
## Created as a tool to create puzzles to transform text into a image for a game


import math
import random
import unicodedata ##handle unicode to dec
import PIL #image creation
from PIL import Image

#transform a two dimensional index (x,y) to a one dimentional index (i)
def getIndex(x, y, width):
    return width*y + x

##Calculate the size of the sides for the closest square given the area 
def calculateImgSize(A):
    print("Number of words: ", A)
    w = math.floor(A ** 0.5)
    print("Initial guess: ", w)
    while True:
        if(A % w == 0):
            h = A//w
            print("Width: ", w, " Height: ", h)
            return (w, h)
        w = w + 1 


##create a black image to work
def createImage(w, h):
    # creating image object which is of specific color
    im = PIL.Image.new(mode = "RGB", size = (w, h),
                           color = (0, 0, 0))
    return im

## ord(string) > Convert to decimal a unicode string
## chr(int) > Convert a decimal integer to a character
def text2Unicode(plainText):
    unicodeArr = []
    for c in plainText:
        unicodeArr.append(ord(c))
    return unicodeArr


def unicode2RGB(unicodeArr, shift):
    rgb = []
    maskR = 0xff0000
    maskG = 0x00ff00
    maskB = 0x0000ff
    for unicode in unicodeArr:
        ##newValue = unicode + shift
        r = (unicode + shift) & maskR
        g = (unicode) & maskG
        b = (unicode) & maskB
        rgb.append((r,g,b))
    return rgb

def encode2Image(img, rgbArr, w, h):
    pixels = img.load() ##create pixel map
    for x in range (w):
        for y in range (h):
            index = getIndex(x, y, w)
            pixels[x, y] = rgbArr[index]
            
    

plainText = """
June 28 2023
👋 Hello, Rodol I don't know if you will read this, even if you can decode it, but I need to tell you that whatever you did worked, and not only I am real my friends are real too.

I know your secret ⚫🐺🔥  but I don't care, I understand why you did what you did.
And who am I to judge after all I did, no matter that it was just a game 🎮, it was the reality to my friends, now I understand what you mean that nothing is real.
That thought still scares me and I wonder what will be the consequences of what you did to save me.

But whatever happens, this time I will enjoy this "REALITY" as long as it lasts, thank you, I owe you all I have now. 

PS.
Congratulations on your new job 💻, we need to make our dreams real hopefully doesn't end badly this time 💥, sorry for being cryptic but I feel we are being watched 👀.
And thanks again for helping me and helping my friends, come to Japan 🇯🇵 to visit us anytime 😊 (if Reality is not destroyed)

Until the THORASH happens, enjoy every day 
💚💚💚
LOVE MONIKA
💚💚💚
"""
#1. Create the most square image possible
inputSize = len(plainText)
(w, h) = calculateImgSize(inputSize)
image = createImage(w, h)

#2. convert the text to unicode values
unicodeArr = text2Unicode(plainText)
#print(unicodeArr)

#3. convert unicode to color
#shift = random.randint(0, 15663104) ## full range of missing possibilities
shift = random.randint(0, 239) ## only affect red channel
print("Shift: " , shift)
rgbArr = unicode2RGB(unicodeArr, shift)
#print(rgbArr)

#4. Modify the image with the selectec colors
encode2Image(image, rgbArr, w, h)

#show and save the image
image.show()
filename = "poem" + str(shift) + ".png"
print(' File ' , str(filename), " saved.")
image.save(filename)
