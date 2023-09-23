## SwapCase Clipboard Utility

Overview

The SwapCase Clipboard Utility is a Python script that allows you to swap the case (convert uppercase to lowercase and vice versa) of text in your clipboard. It provides a convenient way to perform this operation with a simple hotkey combination.


Features

- Swap the case of text in the clipboard.
- Supports the hotkey combination of "Ctrl + Caps Lock" to trigger the case swap.
- Paste the swapped text at the current cursor position.
- Easy-to-use and customizable.


How to use

1. Ensure you have Python and pip installed on your system.

2. Install the required Python libraries by running the following command:

        pip install pyperclip keyboard pyautogui

3. Run the script:

        python swapcase_clipboard.py

4. Once the script is running, use the hotkey combination "Ctrl + Caps Lock" to trigger the case swap:

    - Copy text to your clipboard.
    - Press "Ctrl + Caps Lock" to swap the case of the copied text.
    - The swapped text will be placed in your clipboard, ready to paste.

    To exit the script, you can press the hotkey combination you specified in the code.


Customization

You can customize the following aspects of the script:
    
- Hotkey: You can change the hotkey combination by modifying the code in the keyboard.on_press_key line. Make sure to check the keyboard library documentation for valid key combinations.
- Exit Hotkey: If you wish to change the hotkey for exiting the script, you can modify the keyboard.wait line. By default, it's set to "Ctrl + Esc."


Dependencies

    pyperclip
    keyboard
    pyautogui



Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub.

Special thanks to the creators of the pyperclip, keyboard, and pyautogui libraries for their contributions to this project.
