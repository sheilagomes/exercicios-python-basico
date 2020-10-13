#Demonstração de strings e alguns métodos
#Aspas - 1, 2, 3
x = 'aspas simples - '
y = "aspas duplas - "
z = '''Muitas linhas contidas
em apenas um conjunto
de aspas triplas'''
print(x, y, z)

#Fatiamento
x = '123456789'
print(f'x[:] {x[:]}')
print(f'x[0:2] {x[0:2]}')
print(f'x[:2] {x[:2]}')
print(f'x[4:] {x[4:]}')
print(f'x[4:-1] {x[4:-1]}')
print(f'x[-4:-1] {x[-4:-1]}')
print(f'x[1:2] {x[1:2]}')
print(f'x[2:4] {x[2:4]}')
print(f'x[0:5] {x[0:5]}')
print(f'x[1:8] {x[1:8]}')

#incremento
texto = "era uma vez"
print(f'texto[:] {texto[:]}')
print(f'texto[::2] pular de dois em dois {texto[::2]}')
print(f'texto[::-1] inverter {texto[::-1]}')

#Palíndromos versão minha
texto = input('Digite a palavra: ')
if texto[::-1] == texto:
    print(f'A palavra {texto} é um palíndromo')
else:
    print(f'A palavra {texto} não é um palíndromo')

#Palíndromos versão zumbi
word = input('Type a word: ')
palindrome = word == word[::-1]
print(f'Is the word {word} a palindrome?')
print(palindrome)

#strings são imutáveis
texto, texto2 = 'Exemplo',''
# texto[0] = '@' não funciona mas isso sim:
texto2 = '@' + texto[1:]
print (texto,texto2)

#troca de vogais
palavra = input('Digite uma palavra: ')
k, troca = 0, ''
while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[k]
    k = k + 1
print(troca)

#ver todos os métodos de strings, ajuda específica e tipo
dir('abacate')
help('abacate'.upper)
type('abacate')

#encontrar e substituir
s = 'um tigre, dois tigres, três tigres'
print(f'Pra encontrar 1a. posição\ns.find("tigre") {s.find("tigre")}')
print(f'Pra encontrar 1a. posição depois da posição tal\ns.find("tigre", 4) {s.find("tigre", 4)}')
print('Pra substituir temporariamente s.replace("tigre", "gato")')
print(s.replace('tigre', 'gato'))
print(s)
print('Pra substituir definitivamente s = s.replace("tigre", "gato")')
print(s)
s = s.replace('tigre', 'gato')
print(s)

#Receber uma data em números (dd/mm/aaaa) e escrever por extenso
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
datanum = input('Digite uma data no formato dd/mm/aaa: ')
dia, mes, ano = datanum.split('/')
mes = meses[int(mes)-1]
print(f'{dia} de {mes} de {ano}')

#versão zumbi
meses = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
dia, mes, ano = input('Digite uma data no formato dd/mm/aaa: ').split('/')
print(f'{dia} de {meses[int(mes)-1]} de {ano}')

#Youtube Coding Dojo Globo.com
#Youtube Coding Dojo Muito além do código
