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

def draw_image(file_name):
    clear_output(wait=True)
    image_file = img_dir + file_name
    display(Image.open(image_file))
    sleep(0.1)

def draw_wait_image():
    draw_image('normal/0000.bmp')

def draw_talk_image():
    loop = 2
    while loop > 0:
        for num in range(2):
            draw_image('talk/000' + str(num) + '.bmp')
        loop -= 1
    draw_wait_image()

# TODO
# BaseなのかTalkなのかだけ指定
# 感情をもとにして対応ファイルの候補を出す
# ファイル数をもとにループさせて0から順番に表示させる
# TalkのときはBaseを表示する

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
    draw_wait_image()

def shutdown():
    log.append(text)
    log.append(now() + 'shutdown')
    log.append(text)    
    draw_wait_image()
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
