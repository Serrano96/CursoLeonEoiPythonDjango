LIST = [1,2,3,4,5,6,7,"seis"]
print(LIST)
print(LIST[0])
print(len(LIST))
print(LIST[2:5])
print(LIST[:3])
print(LIST[2:])

size = len(LIST)
print('Tamaño de la lista: ',size)

del LIST[2]
print(LIST)

LIST[2] = 'tres'
print(LIST)
LIST.remove(LIST[0])
print(LIST)