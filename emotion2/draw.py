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
        'wait': ['normal', 'blink', 'lookaround'],
        'talk': 'talk'
    },
    'happy': {
        'wait': ['happy', 'happy_blink', 'giggle'],
        'talk': 'happy_talk'
    },
    'more_happy': {
        'wait': ['more_happy', 'more_happy_blink', 'blush'],
        'talk': 'more_happy_talk'
    },
    'angry': {
        'wait': ['angry', 'knock', 'sigh'],
        'talk': 'angry_talk'
    },
    'more_angry': {
        'wait': ['more_angry', 'snap', 'armfold'],
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

# TODO
# キーワードをもとに該当フォルダ以下を探索
# ファイル数をもとにループさせて0から順番に表示させる
# WaitなのかTalkなのかだけ指定 -> 感情をもとにして対応ファイルの候補　-> Waitのときはランダムで1つを選ぶ

# TODO
# 非同期で画像を表示したい（入力受付中にも画像を切り替えたい）

def draw_talk_image():
    loop = 2
    while loop > 0:
        for num in range(2):
            draw_image('talk/000' + str(num) + '.bmp')
        loop -= 1
    draw_wait_image()

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
