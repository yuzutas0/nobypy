# -*- coding: utf-8 -*-

from unmo import Unmo
from IPython.display import display, clear_output
from PIL import Image
import os
import random
from datetime import datetime


noby = Unmo('noby')
img_dir = '../KOISURU_PROGRAM/sample/emotion/bmps'
text = '*******************************************************'
log = []


def now():
    return datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ")

def prompt(unmo):
    return f"{unmo.name}:{unmo.responder.name} > "

def initialize():
    log.append(text)
    log.append(now() + 'Unmo System prototype : proto')
    log.append(text)

def draw_image():
    clear_output(wait=True)
    image_file = img_dir + '/normal/0000.bmp'
    display(Image.open(image_file))

def draw_text():
    tmp = []
    tmp.extend(log)
    tmp.append('you > \n')
    for raw in reversed(tmp):
        print(raw)

def shutdown():
    log.append(text)
    log.append(now() + 'shutdown')
    log.append(text)    
    draw_image()
    for raw in reversed(log):
        print(raw)
    log.clear()

def logger(input_text):
    if input_text == '':
        return False
    log.append(now() + 'you > ' + input_text)
    log.append(now() + prompt(noby) + noby.dialogue(input_text))
    return True

def start():
    initialize()
    while True:
        draw_image()
        draw_text()
        input_text = input().rstrip()
        if not logger(input_text):
            break
    shutdown()
