import pyautogui, time
from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='x')},
    {keyboard.Key.ctrl, keyboard.KeyCode(char='X')}
]

# The currently active modifiers
current = set()

def execute():
    pyautogui.click(1340, 475)
    time.sleep(1.5)
    pyautogui.click(161, 189)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(1)
    pyautogui.click(683, 457)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

