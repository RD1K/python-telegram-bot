'''
This file includes all of the image processing involved in the program.
'''

HOME_DIRECTORY = ""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Instances of this class are image templates used to make memes
class Template:
    def __init__(self,path,coordinates):
        self.path = path
        self.coordinates = coordinates

    def make_meme(self, userText):
        img = Image.open(self.path)
        draw = ImageDraw.Draw(img)
        size = int(int(img.size[0])*0.045)
        font = ImageFont.truetype((HOME_DIRECTORY + "/telegram-bot/Ubuntu-C.ttf"), size)
        centerx = int(img.size[0])/2
        centery = int(img.size[1])/2
        length = int(len(self.coordinates))
        for spot in range(0, length):
            textSpot = userText[spot].strip()
            draw.text(self.coordinates[spot],textSpot,(255,96,84),font=font)
        img.save(HOME_DIRECTORY + '/sample-out.jpg')

domino_template = Template((HOME_DIRECTORY + "/telegram-bot/domino.jpg"),[(20,36),(260,151)])
