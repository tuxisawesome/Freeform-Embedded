import sys, os
from lib import epd2in13_V3 # Pick driver
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

def dbgprnt(text):
    print(f"(DISPLAY) ==> {text}")

def init_clear():
    epd = epd2in13_V3.EPD()
    dbgprnt("Init and clear display")
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    


def print_screen(text,flip=True):
    init_clear()
    dbgprnt(f"Printing '{text}' to screen...")
    epd = epd2in13_V3.EPD()
    font15 = ImageFont.truetype(f"{os.path.dirname(__file__)}/Font.ttc", 15)
    font24 = ImageFont.truetype(f"{os.path.dirname(__file__)}/Font.ttc", 24)
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font = font24, fill = 0)
    draw.text((0, 28), text, font = font15, fill = 0)
    if flip:
        image = image.rotate(180)
    epd.display(epd.getbuffer(image))



def badge_demo():
    init_clear()
    dbgprnt("Running badge demo")
    epd = epd2in13_V3.EPD()
    font15 = ImageFont.truetype(f"{os.path.dirname(__file__)}/Font.ttc", 15)
    font24 = ImageFont.truetype(f"{os.path.dirname(__file__)}/Font.ttc", 24)
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), "Walter Brobson", font = font24, fill = 0)
    draw.text((0, 28), "Age 13", font = font15, fill = 0)
    draw.text((0, 30), "Current mood: Happy", font = font15, fill = 0)
    
    image = image.rotate(180)
    epd.display(epd.getbuffer(image))


def clock_demo():
    init_clear()
    dbgprnt("Running clock demo")
    font24 = ImageFont.truetype(f"{os.path.dirname(__file__)}/Font.ttc", 24)
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

def sleep():
    epd = epd2in13_V3.EPD()
    dbgprnt("Display sleeping...")
    epd.sleep()