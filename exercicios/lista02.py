#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os
#valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
#equilátero, isósceles ou escaleno.
lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if (lado1 < (lado2 + lado3)) and (lado2 < (lado1 + lado3)) and (lado3 < (lado1 + lado2)) and (lado1 > abs(lado2 - lado3)) and (lado2 > abs(lado1 - lado3)) and (lado3 > abs(lado1 - lado2)):
    if lado1 == lado2 == lado3:
        print('O triângulo é equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Os valores não formam um triângulo')

#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
ano = int(input('Digite o ano: '))
print(ano/4,' ',ano/100,' ',ano/400,' ',str(ano)[-2:])
if ano % 400 == 0:
    print('O ano é bissexto')
elif (ano % 100 != 0) and (ano % 4 == 0):
    print('O ano é bissexto')
elif (str(ano)[-2:] == '00'):
    print('O ano não é bissexto')
else:
    print('O ano não é bissexto')

#3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
#diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
#excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e
#verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da
#multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
peso = float(input('Digite o peso: '))
if peso < 50:
    excesso = multa = 0
else:
    excesso = peso-50
    multa = excesso * 4
print(f'Excesso: {excesso:.2f}  Multa: {multa:.2f}')

#4. Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
if num1 == num2 and num2 == num3:
    print('Os três números são iguais')
elif num1 > num2 and num1 > num3:
    print('O número ',num1,' é maior que ',num2,' e ',num3)
elif num2 > num3:
    print('O número ',num2,' é maior que ',num1,' e ',num3)
else:
    print('O número ',num3,' é maior que ',num1,' e ',num2)

#5. Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
if num1 == num2 and num2 == num3:
    print('Os três números são iguais')
elif num1 > num2 and num1 > num3 and num2 > num3:
    print('O maior número é ',num1,' e o menor é ',num3)
elif num1 > num2 and num1 > num3 and num3 > num2:
    print('O maior número é ',num1,' e o menor é ',num2)
elif num2 > num3 and num2 > num1 and num3 > num1:
    print('O maior número é ',num2,' e o menor é ',num1)
elif num2 > num3 and num2 > num1 and num1 > num3:
    print('O maior número é ',num2,' e o menor é ',num3)
elif num3 > num1 and num3 > num2 and num1 > num2:
    print('O maior número é ',num3,' e o menor é ',num2)
else:
    print('O maior número é ',num3,' e o menor é ',num1)
    
#6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
#mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o
#salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que
#Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme
#a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$
valorHora = int(input('Valor ganho por hora: '))
numHoras = int(input('Número de horas trabalhadas no mês: '))
bruto = valorHora * numHoras
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato
print(f'a. + Salário Bruto : \t R$ {bruto:.2f}')
print(f'b. - IR (11%) : \t R$ {ir:.2f}')
print(f'c. - INSS (8%) : \t R$ {inss:.2f}')
print(f'd. - Sindicato ( 5%) : \t R$ {sindicato:.2f}')
print(f'e. = Salário Liquido : \t R$ {liquido:.2f}')

#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
#da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
#quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um
#número inteiro de latas.
metros = int(input('Quantos metros quadrados? '))
if metros % 54 == 0:
    latas = metros/54
else:
    latas = int(metros/54) + 1
print(f'É preciso comprar {int(latas)} lata(s) que totalizam R$ {latas*80:.2f}')
