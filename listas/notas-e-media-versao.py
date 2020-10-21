#versão 1
notas = []
k = 1
while k <= 4:
    notas.append(float(input('Nota: ')))
    k = k + 1
soma = k = 0
while k <= 3:
    soma = soma + notas[k]
    k = k + 1
print(f'Média {notas} é {soma/4:.1f}')

#versão 2
notas = []
k, soma = 0, 0
while k <= 3:
    notas.append(float(input('Nota: ')))
    soma = soma + notas[k]
    k = k + 1
print(f'Média {notas} é {soma/4:.1f}')
