#separar strings com for
def épar(x):
    return x%2 == 0
print(épar(13))
print(épar(12))

#calcular o fatorial de 1 número lido
def fatorial(x):
    fat = 1
    while x > 0:
        fat = fat * x
        x = x - 1
    return fat
print(fatorial(10))

#alterando string
José = 'entrou 6h'
def fatec():
    José = 'entrou 8h'
    print (José)
print (José)
fatec()
print (José)

#alterando global
José = 'entrou 6h'
def fatec():
    global José
    José = 'entrou 8h'
    print (José)
print (José)
fatec()
print (José)

#numeros e nomes aleatórios
import random
print(random.randint(1,100))
nomes='zé lia pedro luiz maria thi'.split()
print(random.choice(nomes))
random.shuffle(nomes)
print (nomes)
print(random.sample(range(100), 10))
