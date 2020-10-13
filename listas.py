#Demonstração de listas e alguns métodos
edificio = ["Família Gomes", "Família chata", "Amanda e Lúcio", "Caixa d'água"]
print(edificio[0])
print(edificio[1])
print(edificio[2])
print(edificio[3])
edificio.append("Família fantasma")
print(f'O edificio tem {len(edificio)} apartamentos, ocupados por {edificio[0]}, {edificio[1]}, {edificio[2]}, {edificio[3]}, {edificio[4]}')

#Notas e média versão 1
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

#Notas e média versão 2
notas = []
k, soma = 0, 0
while k <= 3:
    notas.append(float(input('Nota: ')))
    soma = soma + notas[k]
    k = k + 1
print(f'Média {notas} é {soma/4:.1f}')
