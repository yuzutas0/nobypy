# -*- coding: utf-8 -*-

class Responder():
    def __init__(self, name):
        self.name = name
    
    def response(self, input_text):
        return f"{input_text}ってなに？"


class Unmo():
    def __init__(self, name):
        self.name = name
        self.responder = Responder('What')
    
    def dialogue(self, input_text):
        return self.responder.response(input_text)


def prompt(unmo):
    return f"{unmo.name}:{unmo.responder.name} > "

print('Unmo System prototype : proto')
proto = Unmo('proto')

while True:
    print('> ')
    input_text = input()
    input_text = input_text.rstrip()
    if input_text == '':
        break
    response = proto.dialogue(input_text)
    print(prompt(proto) + response)


print('shutdown')
