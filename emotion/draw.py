# -*- coding: utf-8 -*-

from unmo import Unmo
from IPython.display import display, clear_output
from PIL import Image
import os
import random
from datetime import datetime
from time import sleep


noby = Unmo('noby')
img_dir = '../KOISURU_PROGRAM/sample/emotion/bmps/'
text = '*******************************************************'
log = []


def now():
    return datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ")

def prompt(unmo):
    return f"{unmo.name}:{unmo.responder.name} > "

def draw_image(file_name):
    clear_output(wait=True)
    image_file = img_dir + file_name
    display(Image.open(image_file))
    sleep(0.1)

def draw_normal_image():
    draw_image('normal/0000.bmp')

def draw_talk_image():
    loop = 2
    while loop > 0:
        for num in range(2):
            draw_image('talk/000' + str(num) + '.bmp')
        loop -= 1
    draw_normal_image()

def draw_text():
    tmp = []
    tmp.extend(log)
    tmp.append('you > \n')
    for raw in reversed(tmp):
        print(raw)

def initialize():
    log.append(text)
    log.append(now() + 'Unmo System prototype : proto')
    log.append(text)
    draw_normal_image()

def shutdown():
    log.append(text)
    log.append(now() + 'shutdown')
    log.append(text)    
    draw_normal_image()
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
        draw_text()
        input_text = input().rstrip()
        if not logger(input_text):
            break
        draw_talk_image()
    shutdown()
