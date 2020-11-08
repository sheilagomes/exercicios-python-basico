#script para copiar texto do OmegaT ao Crow e de volta
'''
import pyautogui, time
def tra():
    pyautogui.hotkey('ctrl', 'alt', 'e')
    time.sleep(1.5)
    pyautogui.click(582, 323)
    time.sleep(0.5)
    pyautogui.click(260, 423)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
tra()
'''
#script para copiar texto do Memsource ao Crow e de volta
#Condições: estar com cursor no segmento e selecionado e copiado (Ctrl + A e Ctrl + X)
import pyautogui, time
def tra():
#    x, y = pyautogui.position()
    pyautogui.hotkey('ctrl', 'alt', 'e')
    time.sleep(1.5)
    pyautogui.click(161, 189)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    time.sleep(1)
    pyautogui.click(683, 434)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
tra()
