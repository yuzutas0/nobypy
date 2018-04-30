# -*- coding: utf-8 -*-

from unmo import Unmo
from IPython.display import Image, display_png, clear_output
import os
import random


def prompt(unmo):
    return f"{unmo.name}:{unmo.responder.name} > "


def start():
    print('Unmo System prototype : proto')
    noby = Unmo('noby')
    log = ''
    files = os.listdir('../images')

    while True:
        clear_output(wait=True)
        image_file = '../images/' + random.choice(files)
        display_png(Image(image_file))
        print(log)
        print('> ')
        input_text = input()
        input_text = input_text.rstrip()
        if input_text == '':
            break
            response = noby.dialogue(input_text)
            log = log + 'you > ' + input_text + '\n' + prompt(noby) + response + '\n'

    print('shutdown')
