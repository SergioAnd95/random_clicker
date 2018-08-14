from random import randint
from time import sleep

import pyautogui

keys = [
    'ctrlleft',
    'ctrlright',
    'shiftleft',
    'shiftright',
    'up',
    'down',
    'left',
    'rigtht',
    'option',
    'command'
]

width, height = pyautogui.size()
middle_x, middle_y = width/2, height/2

l = len(keys) - 1


print('Press Ctrl-C to quit')

try:
    while True:
        click = randint(1, 2)

        if click == 1:
            pyautogui.click(x=middle_x, y=middle_y)
            print('Mouse click!!!')
        else:
            key_num = randint(0, l)
            pyautogui.press(keys[key_num])
            print('Press %s' % keys[key_num])

        time_sleep = randint(1, 3) # randomize sleep time
        sleep(time_sleep)
except KeyboardInterrupt:
    print('\nDone')
