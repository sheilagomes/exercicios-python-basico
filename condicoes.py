a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print('O primeiro número é o maior')
if b > a:
    print('O segundo número é o maior')
        
idade=int(input('Digite a idade: '))
if idade <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')

velocidade = int(input('Digite a velocidade: '))
if velocidade >110:
    multa=(velocidade-110)*5
    print(f'Você foi multado em R$ {multa:.2f}')
else:
    print('Siga em frente')

min = float(input('Digite os minutos: '))
if min < 200:
    conta = min * 0.20
else:
    if min <= 400:
        conta = min * 0.18
    else:
        conta = min * 0.15
print(f'Sua conta totalizou R$ {conta:.2f}')

min = float(input('Digite os minutos: '))
if min < 200:
    conta = min * 0.20
elif min <= 400:
    conta = min * 0.18
elif min <= 800:
    conta = min * 0.15
else:
    conta = min * 0.08
print(f'Sua conta totalizou R$ {conta:.2f}')

