#Aspas - 1, 2, 3
x = 'aspas simples - '
y = "aspas duplas - "
z = '''Muitas linhas contidas
em apenas um conjunto
de aspas triplas'''
print(x, y, z)
#strings são imutáveis
texto, texto2 = 'Exemplo',''
# texto[0] = '@' não funciona mas isso sim:
texto2 = '@' + texto[1:]
print (texto,texto2)
#ver todos os métodos de strings, ajuda específica e tipo
dir('abacate')
help('abacate'.upper)
type('abacate')
