import random

for n in range(10):
    print('entero aleatorio: ', random.randint(10,20))

for n in range(4):
    print(random.random())

L = ['Oscar','Lucia','Jaime','Pepe','Cris','yolanda','taimi']

for n in range(8):
    print(random.choice(L))

random.shuffle(L)

print(random.sample(L,k=2))