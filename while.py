#imprimir números de 1 até o limite inserido
limite = int(input('Digite o número limite: '))
x = 1
while x <= limite:
    print(x)
    x = x + 1

#imprimir os números pares de 1 até o limite inserido
limite = int(input('Digite o número limite: '))
x = 0
while x <= limite:
    print(x)
    x = x + 2

#imprimir a soma de 10 números lidos
x = 1
soma = 0
while x <=10:
    numero = int(input(f'Digite o numero {x}: '))
    soma = soma + numero
    x = x +1
print(f'Soma: {soma}')

#calcular a média de 10 números lidos
x = 1
soma = 0
while x <=10:
    numero = int(input(f'Digite o numero {x}: '))
    soma = soma + numero
    x = x +1
print(f'Média: {soma/10:.1f}')

#calcular o fatorial de 1 número lido
x = 1
fat = 1
numero = int(input('Digite o fatorial: '))
while x <=numero:
    fat = fat * x
    x = x +1
print(f'O fatorial de {numero} é {fat}')

#calcular a média dos valores digitados
soma = 0
x = 0
while True:
    numero = int(input('n (zero sai): '))
    if numero == 0 :
        break
    soma = soma + numero
    x = x +1
print(f'A média dos valores digitados é {soma/x}')

#tabuada
t = 1
while t <= 10:
    print(f'Tabuado do {t}')
    n = 1
    while n <= 10:
        print(f'{t} x {n} = {t*n}')
        n = n + 1
    t = t + 1
    print()
