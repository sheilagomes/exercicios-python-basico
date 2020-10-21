def fatorial(x):
    fat = 1
    while x > 0:
        fat = fat * x
        x = x - 1
    return fat
print(fatorial(10))
