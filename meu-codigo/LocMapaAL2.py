import pyautogui, time, clipboard
from pynput import keyboard

COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='c')},
    {keyboard.Key.ctrl, keyboard.KeyCode(char='C')}
]

current = set()

coor = [[434, 529, 41], [370, 515, 39], [405, 458, 45], [401, 377, 45], [435, 521, 45], [372, 386, 45], [336, 372, 53], [355, 343, 53], [320, 368, 53], [352, 420, 53], [315, 360, 53], [380, 352, 55], [334, 356, 53], [272, 330, 43], [348, 370, 53], [349, 385, 53], [432, 487, 43], [359, 431, 43], [401, 348, 53], [385, 348, 53]]
paises = ['argentina', 'chile', 'bolívia', 'venezuela', 'uruguai', 'colômbia', 'costa rica', 'cuba', 'el salvador', 'equador', 'guatemala', 'haiti', 'honduras', 'méxico', 'nicarágua', 'panamá', 'paraguai', 'peru', 'porto rico', 'república dominicana']

def execute(x, y, z):
    pyautogui.click(983, 384)
    pyautogui.click(134, 54)
    time.sleep(0.5)
    pyautogui.click(135, 97)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyautogui.scroll(z)
    time.sleep(1)
    pyautogui.click(637, 527)
    time.sleep(0.5)
    pyautogui.dragTo(983, 384)
    time.sleep(0.5)
    pyautogui.click(1338, 55)

def pais():
    a = 0
    pais = clipboard.paste()
    print(pais)
    if pais.lower() in paises:
        a = paises.index(pais)
        print(pais)
        execute(coor[a][0], coor[a][1], coor[a][2])

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            pais()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
