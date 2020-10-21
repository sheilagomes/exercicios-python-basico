min = float(input('Digite os minutos: '))
if min < 200:
    conta = min * 0.20
elif min <= 400:
    conta = min * 0.18
elif min <= 800:
    conta = min * 0.15
else:
    conta = min * 0.08
print(f'Sua conta totalizou R$ {conta:.2f}')
