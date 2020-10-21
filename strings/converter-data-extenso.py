meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
datanum = input('Digite uma data no formato dd/mm/aaa: ')
dia, mes, ano = datanum.split('/')
mes = meses[int(mes)-1]
print(f'{dia} de {mes} de {ano}')

#versão zumbi
meses = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
dia, mes, ano = input('Digite uma data no formato dd/mm/aaa: ').split('/')
print(f'{dia} de {meses[int(mes)-1]} de {ano}')

#Youtube Coding Dojo Globo.com
#Youtube Coding Dojo Muito além do código
