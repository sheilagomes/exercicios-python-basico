min = float(input('Digite os minutos: '))
if min < 200:
    conta = min * 0.20
else:
    if min <= 400:
        conta = min * 0.18
    else:
        conta = min * 0.15
print(f'Sua conta totalizou R$ {conta:.2f}')
