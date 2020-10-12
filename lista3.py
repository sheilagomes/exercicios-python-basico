#3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
#crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B,
#mantidas as taxas de crescimento

#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
#formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
#de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.

#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
#o algoritmo de Euclides.

#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    numero = int(input('Digite um número entre 0 e 10: '))
    if numero < 0 or numero > 10:
        print('O número é inválido')
    else:
        break
    
#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    if nome == senha:
        print('A senha não pode ser igual ao nome, tente de novo')
    else:
        break
