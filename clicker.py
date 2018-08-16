import asyncio
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
    'alt'
]

width, height = pyautogui.size()
middle_x, middle_y = width/2, height/2

async def change_screen():
    while True:
        pyautogui.keyDown('ctrlleft')
        pyautogui.press(']')
        pyautogui.keyUp('ctrlleft')
        time_sleep = randint(60, 240)
        print('Next Tab!!!')
        await asyncio.sleep(time_sleep)


async def keyboard_mouse_click():
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
        await asyncio.sleep(time_sleep)


l = len(keys) - 1

print('Press Ctrl-C to quit')

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        keyboard_mouse_click(),
        change_screen()
    ))
except KeyboardInterrupt:
    loop.close()
    print('\nDone')
