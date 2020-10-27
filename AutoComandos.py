import pyautogui, time
def tra():
    pyautogui.hotkey('ctrl', 'alt', 'e')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
tra()
