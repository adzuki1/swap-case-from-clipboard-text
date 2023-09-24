# case switch transforma um texto copiado em uppercase ou lowercase

import pyperclip
import keyboard
import pyautogui

def swapCase(text):
    return text.swapcase()


def isPressed():
    capslock_state = keyboard.is_pressed('caps lock')
    ctrl_state = keyboard.is_pressed('ctrl')

    if(capslock_state and ctrl_state):
        clipboard_txt = pyperclip.paste()
        swapped_txt = swapCase(clipboard_txt)

        pyperclip.copy(swapped_txt)

        pyautogui.hotkey('ctrl', 'v')


keyboard.on_press_key('caps lock', lambda _: isPressed)
#keyboard.wait()
