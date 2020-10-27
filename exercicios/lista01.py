#1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
print(f'A soma de {num1} e {num2} é {num1+num2}')

#2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
metros = float(input('Digite um valor em metros: '))
print(f'{metros:.2f} metros equivale a {metros*1000:.0f} milímetros')

#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#   Calcule o total em segundos.
dias = int(input('Digite o número de dias: '))
horas = int(input('Digite o número de horas: '))
minutos = int(input('Digite o número de minutos: '))
segundos = int(input('Digite o número de segundos: '))
total = (dias*24*3600)+(horas*3600)+(minutos*60)+segundos
print(f'O total em segundos é {total}')

#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#   porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input('Digite o valor do salário: '))
porcentagem = float(input('Digite a porcentagem do aumento: '))
aumento = salario * (porcentagem/100)
print(f'O valor do aumento é de R$ {aumento:.2f}')
print(f'O valor do salário com o aumento é de R$ {salario+aumento:.2f}')

#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#   preço a pagar.
preço = float(input('Digite o preço: '))
percentual = float(input('Digite o percentual de desconto: '))
desconto = preço * (percentual/100)
print(f'O valor do desconto é de R$ {desconto:.2f}')
print(f'O preço a pagar é de R$ {preço-desconto:.2f}')

#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#   esperada para a viagem.
distancia = float(input('Digite a distância: '))
velocidade = float(input('Digite a velocidade média: '))
tempo = distancia / velocidade
print(f'O tempo da viagem será de {tempo:.1f} horas')

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
celsius = float(input('Digite a temperatura em graus Celsius: '))
farenheit = (9*celsius/5) + 32
print(f'A temperatura equivale a {farenheit:.2f} em graus Farenheit')

#8) Faça agora o contrário, de Fahrenheit para Celsius.
farenheit = float(input('Digite a temperatura em graus Farenheit: '))
celsius = (farenheit-32)*5/9
print(f'A temperatura equivale a {celsius:.2f} em graus Celsius')

#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#   usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a
#   pagar,sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
km = float(input('Digite a quantidade de km percorridos: '))
dias = float(input('Digite a quantidade de dias: '))
locação = (dias * 60) + (km * 0.15)
print(f'O valor da locação é de R$ {locação:.2f}')

#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#   quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#   perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba
#   o total de dias.
cigarros = float(input('Digite a quantidade de cigarros fumados por dia: '))
anos = float(input('Digite há quantos anos fuma: '))
perda = (((cigarros * 10)/60)/24)*(anos*365)
print(f'O fumante perdeu {perda} dias de vida')

#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2
#   elevado a um milhão.
print(len(str(2 ** 1000000)))
