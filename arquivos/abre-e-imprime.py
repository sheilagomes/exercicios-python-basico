#versão 1
f = open(r'/home/sheila/xxx.txt')
for linha in f.readlines():
    #tira o \n de cada linha p/ñ pular 1 linha a mais
    print(linha.strip())
f.close()

#versão 2
with open(r'/home/sheila/xxx.txt') as f:
    print(f.read())
