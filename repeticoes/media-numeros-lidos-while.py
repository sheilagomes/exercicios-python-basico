#versão 1
x = 1
soma = 0
while x <=10:
    numero = int(input(f'Digite o numero {x}: '))
    soma = soma + numero
    x = x +1
print(f'Média: {soma/10:.1f}')

#versão 2
soma = 0
x = 0
while True:
    numero = int(input('n (zero sai): '))
    if numero == 0 :
        break
    soma = soma + numero
    x = x +1
print(f'A média dos valores digitados é {soma/x}')
