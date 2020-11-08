#abrir o mapa no início
#selecionar nome do país e ter atalho para rodar
#Ctrl + x armazena em variável, converte pra minúsculo, busca na lista de países e roda, ver pynput como armazena com ctrl + x
#ter condição para verificar uma lista de países OK
#abrir o mapa em tela cheia e levar ao país no mapa OK
#aumentar o zoom com ctrl e rolagem de mouse? clicando na opção de zoom? OK com rolagem
'''
434, 529, 41 - Argentina
370, 515, 39 - Chile
405, 458, 45 - Bolívia
401, 377, 45 - Venezuela
435, 521, 45 - Uruguai
372, 386, 45 - Colômbia
336, 372, 53 - Costa Rica
355, 343, 53 - Cuba
320, 368, 53 - El Salvador
352, 420, 53 - Equador
315, 360, 53 - Guatemala
380, 352, 55 - Haiti
334, 356, 53 - Honduras
272, 330, 43 - México
348, 370, 53 - Nicarágua
349, 385, 53 - Panamá
432, 487, 43 - Paraguai
359, 431, 43 - Peru
401, 348, 53 - Porto Rico
385, 348, 53 - República Dominicana
134, 54 - Abrir menu zoom
135, 97 - Best fit
116, 213 - 133%
'''

import pyautogui, time

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

pais, a = ' ', 0

while pais !='':
    pais = input('País: ').lower()
    if pais.lower() in paises:
        a = paises.index(pais)
        execute(coor[a][0], coor[a][1], coor[a][2])
