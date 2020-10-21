#1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
#as funções max e min.
from random import sample
lista = sample(range(100),10)
maior = menor = lista[0]
for i in range(10):
    if lista[i] >= maior: maior = lista[i]
    if lista[i] <= menor: menor = lista[i]
print(lista)
print(f'O maior número da lista é {maior} e o menor é {menor}')

#2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
#números ímpares na lista IMPAR. Imprima as três listas.
from random import sample
lista = sample(range(100),20)
PAR, IMPAR = [],[]
for i in range(20):
    if lista[i] % 2 == 0: PAR.append(lista[i])
    else: IMPAR.append(lista[i])
print(lista)
print(PAR)
print(IMPAR)

#2 - versão zumbi com list comprehension
from random import sample
lista = sample(range(100),20)
PAR = [x for x in lista if x % 2 == 0]
IMPAR = [x for x in lista if x % 2 == 1]
kprint(lista)
print(PAR)
print(IMPAR)

#3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
#terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
#intercalados dos dois outros vetores. Imprima os três vetores.
from random import sample
lista1, lista2, lista3 = sample(range(100),10), sample(range(100),10), []
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista1)
print(lista2)
print(lista3)

#3 - versão zumbi
from random import sample
lista1, lista2, lista3 = sample(range(100),10), sample(range(100),10), []
for i in zip(lista1, lista2):
    lista3.extend(list(i))
print(lista1)
print(lista2)
print(lista3)

#4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
#community welcome and encourage participation by everyone. Our community is based on
#mutual respect, tolerance, and encouragement, and we are working to help each other live up
#to these principles. We want our community to be more diverse: whoever you are, and
#whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
#split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
#“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
#e cuidado com maiúsculas e minúsculas.
lista1 ='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
lista1, lista2 = lista1.lower().split(' '), []
for i in range(len(lista1)):
    if ',' in lista1[i] or '.' in lista1[i] or ':' in lista1[i]:
        lista1[i] = lista1[i][:-1]
    if lista1[i][0:1] in 'python' or lista1[i][-2:-1] in 'python':
        lista2.append(lista1[i])
print(lista1)
print(lista2)

#4 - versão zumbi - 1
texto ='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
resp = []
for p in texto.split():
    if p[0] in 'python' or p[-1] in 'python':
        resp.append(p)
print(resp)

#4 - versão zumbi - 2 com list comprehension
texto ='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
resp = [p for po in texto.split()
    if p[0] in 'python' or p[-1] in 'python']
print(resp)

#5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
#“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
#minúsculas e de remover antes os caracteres especiais.
lista1 ='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
lista1, lista2, tem = lista1.lower().split(' '), [], False
for i in range(len(lista1)):
    if ',' in lista1[i] or '.' in lista1[i] or ':' in lista1[i]:
        lista1[i] = lista1[i][:-1]
    for k in range(len(lista1[i])):
        if lista1[i][k] in 'python' and len(lista1[i]) > 4:
            tem = True
    if tem:
        lista2.append(lista1[i])
        tem = False
print(lista2)    
print(f'Existem {len(lista2)} palavras com uma das letras de "python" e mais de 4 caracteres')

#5 - versão zumbi 1
texto ='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')

def pitônica(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False

resp = []
for p in texto.split()
if pitônica(p) and len(p) > 4:
    resp.append(p)
print(resp)

#5 - versão zumbi 2
texto ='''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')

def pitônica(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False

resp = [p ofr p in texto.split()
        if pitônica(p) and len(p) > 4]
print(resp)
print(len(resp))
