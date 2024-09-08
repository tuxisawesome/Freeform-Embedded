import sys

from lib import epd2in13_V3 # Pick driver
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

def init_clear():
    epd = epd2in13_V3.EPD()
    print("(DISPLAY) ==> init and Clear disp")
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    


def print_screen(text):
    init_clear()
    epd = epd2in13_V3.EPD()
    font15 = ImageFont.truetype("../fonts/Font.ttc", 15)
    font24 = ImageFont.truetype("../fonts/Font.ttc", 24)
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    draw.text((120, 60), text, font = font15, fill = 0)
    epd.display(epd.getbuffer(image))


def clock_demo():
    init_clear()
    font24 = ImageFont.truetype("../fonts/Font.ttc", 24)
    epd = epd2in13_V3.EPD()
    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)
    
    epd.displayPartBaseImage(epd.getbuffer(time_image))
    num = 0
    while (True):
        time_draw.rectangle((120, 80, 220, 105), fill = 255)
        time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        epd.displayPartial(epd.getbuffer(time_image))
        num = num + 1
        if(num == 10):
            break