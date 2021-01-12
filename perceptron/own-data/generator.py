from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import sys
import inspect

# code for import multi_layer_perceptron from parent folder
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Variables

# The text that will be displayed on the generated image
generate_for_symbol = "K"
# Path to the system fonts
font_locations = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts"]
# Text font size
font_size = 38
img_size = (70, 70)
text_position = (18, 18)
result_folder = "{}/train_{}/".format(current_dir, generate_for_symbol)

def createImg(fontPath, font_size, text, result_folder):
    try:
        font = ImageFont.truetype(fontPath, font_size)

        img = Image.new('RGB', img_size, (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(text_position, text, fill=(0, 0, 0), font=font)
        img.save("{}/{}_{}.png".format(result_folder, text, font.font.family))
    except:
        print("Oops! enable to creare img for " + fontPath)

def loadFontAndCreateImg(font_folder):
    global images
    fonts = os.listdir(font_folder)
    fonts = list(filter(lambda x: x.endswith(".ttf"), fonts))
    for i in range(len(fonts)):
        fontName = fonts[i]
        createImg(font_folder + fontName, font_size, generate_for_symbol, result_folder)

if not os.path.exists(result_folder):
    os.makedirs(result_folder)

for i in range(len(font_locations)):
    font_folder = font_locations[i]
    loadFontAndCreateImg(font_folder)