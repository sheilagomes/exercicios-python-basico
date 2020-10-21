velocidade = int(input('Digite a velocidade: '))
if velocidade >110:
    multa=(velocidade-110)*5
    print(f'Você foi multado em R$ {multa:.2f}')
else:
    print('Siga em frente')
