#4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos
#calculando também a multiplicidade de cada fator.

#1. Dizemos que um número natural é triangular se ele é produto de três números naturais
#consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
#verificar se n é triangular.
tri = int(input('Digite um número inteiro: '))
a, b, c, t = 1, 2 , 3, False
while a * b * c <= tri:
    print(f'{a} * {b} * {c} = {a * b * c}')
    if a * b * c == tri:
        t = True
    a, b, c = a + 1, b + 1, c + 1
if t:
    print(f'O número {tri} é tringular')
else:
    print(f'O número {tri} não é tringular')

#2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
#algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
#os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
#nenhuma delas esteja em falta no caixa.
dif, cinquenta, vinte, dez, cinco, dois, um = 0, 0, 0, 0, 0, 0, 0
conta = int(input('Digite o valor da conta: '))
pago = int(input('Digite o valor pago: '))
troco = pago - conta

dif, troco = troco, troco % 50
if troco >= 0:
    cinquenta = int(dif / 50)

dif, troco = troco, troco % 20
if troco >= 0:
    vinte = int(dif / 20)

dif, troco = troco, troco % 10
if troco >= 0:
    dez = int(dif / 10)

dif, troco = troco, troco % 5
if troco >= 0:
    cinco = int(dif / 5)

dif, troco = troco, troco % 2
if troco >= 0:
    dois = int(dif / 2)
    um = troco

print(f'O troco de R$ {pago - conta:.2f} equivale a:\n{cinquenta} nota(s) de cinquenta\n{vinte} nota(s) de vinte\n{dez} nota(s) de dez\n{cinco} nota(s) de cinco\n{dois} nota(s) de dois\n{um} nota(s) de um')

#3. Verifique se um inteiro positivo n é primo.
numero = int(input('Digite um número inteiro positivo: '))
cont, primo = 2, True
while cont < numero:
    if numero % cont == 0:
        primo = False;
    cont = cont + 1
if (primo):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')

#5. Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
numero = input('Digite um numero inteiro positivo: ')
x = len(numero)-1
novo = ""
while x >= 0:
    novo = novo + numero[x]
    x = x - 1
print(novo)
