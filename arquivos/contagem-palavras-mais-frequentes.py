import string
#abre o texto e deixa tudo minúsculo
texto = open('alice.txt').read().lower()
#tira toda a pontuação
for c in string.punctuation:
    texto = texto.replace(c, ' ')
#divide em uma lista
palavras = texto.split()
#cria o dicionário, conta as palavras e acrescenta
wc = {}
for p in palavras:
    if p in wc:
        wc[p] += 1
    else:
        wc[p] = 1

##def contador(dupla):
##    return dupla[1]

#ordena por número de ocorrências e mostra 20 primeiras
duplas = sorted(wc.items(),
                key=lambda dupla:dupla[1],
                reverse=True)
for dupla in duplas[:20]:
    print (dupla[0], dupla[1])
