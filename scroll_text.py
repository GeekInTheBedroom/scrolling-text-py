import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def scroll_text(text: str, delay: float):
    for i in range(len(text)):
        spaces = ' ' * (len(text) - i)
        print(f"{spaces}{text[:i]}")
        time.sleep(delay)
        clear_screen()

    for i in range(len(text)):
        print(text[i:])
        time.sleep(delay)
        clear_screen()

# testing
clear_screen()
while True:
    scroll_text("PYTHON", 0.5)

"""
If you can optimize this, please do it.
I hope that this code could at least be used for your school project or something :)
This is so useless. I don't even know why I did this.
"""
