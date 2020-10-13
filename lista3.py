#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = float(input('Digite uma nota entre 0 e 10: '))
while nota < 0 or nota > 10:
    print('A nota deve estar entre 0 e 10, tente de novo')
    nota = float(input('Digite uma nota entre 0 e 10: '))
    
#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
while nome == senha:
    print('A senha não pode ser igual ao nome, tente de novo')
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

#3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
#crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B,
#mantidas as taxas de crescimento
a, b, anos = 80000, 200000, 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print(f'Em {anos} anos, o país A terá {a:.0f} habitantes e o país B, {b:.0f}')

#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
#formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
#de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.
#Youtube Nature by Numbers
#atribuição múltipla a,b = b, a + b
f, a, b = 0, 0, 1
numero=int(input('Digite um número inteiro: '))
while f < numero:
    a,b = b, a + b
    f = f + 1
print(f'O {numero}o. número de Fibonacci é {a}')

#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
#o algoritmo de Euclides. 5:53
num1 = int(input('Digite um número inteiro positivo: '))
num2 = int(input('Digite outro número inteiro positivo: '))
a, b = num1, num2
while a % b !=0:
    a, b = b, a % b
print(f'O máximo divisor comum entre {num1} e {num2} é {b}')
