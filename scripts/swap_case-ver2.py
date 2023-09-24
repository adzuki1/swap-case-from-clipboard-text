import pyperclip
import keyboard
import pyautogui

def swapCase(text):
    '''swap case from copied text'''

    return text.swapcase()

def isPressed():
    '''checks if hotkey was pressed'''

    caps_lock_state = keyboard.is_pressed('caps lock')
    ctrl_state = keyboard.is_pressed('ctrl')

    if caps_lock_state and ctrl_state:
        # switch clipboard text with current
        clipboard_text = pyperclip.paste()
        swapped_text = swapCase(clipboard_text)
        pyperclip.copy(swapped_text)

        # paste clipboard current text
        pyautogui.hotkey('ctrl', 'v')

# Listener
keyboard.on_press_key('caps lock', lambda _: isPressed())

# keeps program running
keyboard.wait() # we can add a hotkey to end program