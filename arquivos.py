#cria arquivo e popula
f = open(r'/home/sheila/xxx.txt', 'w')
for linha in range(1,101):
    f.write(f'{linha}\n')
f.close()

#abre arquivo e imprime conteúdo
f = open(r'/home/sheila/xxx.txt')
for linha in f.readlines():
    #tira o \n de cada linha p/ñ pular 1 linha a mais
    print(linha.strip())
f.close()

#abre arquivo e imprime conteúdo - opção curta
with open(r'/home/sheila/xxx.txt') as f:
    print(f.read())

#abrir arquivo e trocar vogais por *
texto = open('mensagem.txt', 'r')
cripto = open('cripto.txt', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouãõ':
            cripto.write('*')
        else:
            cripto.write(letra)
texto.close()
cripto.close()

#verifica IPs válidos e inválidos
def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True

arq = open('IPS.txt')
validos = open('Válidos.txt', 'w')
invalidos = open('Inválidos.txt', 'w')
for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()

#contagem de palavras mais frequentes em um texto
import string
#abre o texto e deixa tudo minúsculo
texto = open('alice.txt').read().lower()
#tira toda a pontuação
for c in string.punctuation:
    texto = texto.replace(c, ' ')
#dive em uma lista
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
