import random
print(random.randint(1,100))
nomes='zé lia pedro luiz maria thi'.split()
print(random.choice(nomes))
random.shuffle(nomes)
print (nomes)
print(random.sample(range(100), 10))
