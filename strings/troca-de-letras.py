palavra = input('Digite uma palavra: ')
k, troca = 0, ''
while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[k]
    k = k + 1
print(troca)
