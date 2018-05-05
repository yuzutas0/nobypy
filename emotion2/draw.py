# -*- coding: utf-8 -*-

from unmo import Unmo
from IPython.display import display, clear_output
from PIL import Image
import os
import random
from datetime import datetime
from time import sleep


noby = Unmo('noby')
img_dir = '../KOISURU_PROGRAM/sample/emotion2/bmps/'
text = '*******************************************************'
log = []
images = {
    'normal': {
        'base': 'normal',
        'move': ['blink', 'lookaround'],
        'talk': 'talk'
    },
    'happy': {
        'base': 'happy',
        'move': ['happy_blink', 'giggle'],
        'talk': 'happy_talk'
    },
    'more_happy': {
        'base': 'more_happy',
        'move': ['more_happy_blink', 'blush'],
        'talk': 'more_happy_talk'
    },
    'angry': {
        'base': 'angry',
        'move': ['knock', 'sigh'],
        'talk': 'angry_talk'
    },
    'more_angry': {
        'base': 'more_angry',
        'wait': ['snap', 'armfold'],
        'talk': 'more_angry_talk'
    }
}


def now():
    return datetime.now().strftime("[%Y/%m/%d %H:%M:%S] ")

def prompt(unmo):
    return f"{unmo.name}:{unmo.responder.name} > "

def feeling():
    mood = noby.emotion.mood
    if -5 <= mood and mood <= 5:
        return 'normal'
    elif 5 < mood and mood <= 10:
        return 'happy'
    elif 10 < mood:
        return 'more_happy'
    elif -10 <= mood and mood < -5:
        return 'angry'
    elif mood < -10:
        return 'more_angry'
    return None

def image_file_count(path):
    count = 0
    for name in os.listdir(path):
        if(name[-4:] == '.bmp'):
            count = count + 1
    return count

def draw_image(file_name):
    clear_output(wait=True)
    image_file = img_dir + file_name
    display(Image.open(image_file))
    sleep(0.1)

def draw_base_image():
    feel = feeling()
    path = images[feel]['base'] + '/0000.bmp'
    draw_image(path)

def draw_talk_image():
    feel = feeling()
    path = images[feel]['talk']
    count = image_file_count(img_dir + path)
    for i in range(count):
        draw_image(path + '/000' + str(i) + '.bmp')
    draw_base_image()

# TODO
# 非同期で画像を表示したい（入力受付中にも画像を切り替えたい）
# Move になったり Baseになったり
# Moveのときはランダムで1つ選ぶ

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
    draw_base_image()

def shutdown():
    log.append(text)
    log.append(now() + 'shutdown')
    log.append(text)    
    draw_base_image()
    for raw in reversed(log):
        print(raw)
    log.clear()
    noby.emotion.clear()

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
