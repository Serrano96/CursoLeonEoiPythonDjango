class Thing:
    pass

thing = Thing()

class Fruit:
    def __init__(self):
        print('objeto fruta')

fruit = Fruit()

class CustomFruit():
    COUNTER = 0
    def __init__ (self,name,color):
        self.name = name
        self.color = color
        self.juices = 0
        CustomFruit.COUNTER += 1

    def __str__(self):
        return 'Soy fruta me llamo {} y mi color es {}.\nHay {} frutas en total'\
        .format(self.name,self.color,CustomFruit.COUNTER)

    def make_juice(self,count):
        for n in range(count):
            print('Haciendo zumo de ',self.name)
            self.juices +=1

custom = CustomFruit('Pera','verde')
c2 = CustomFruit('Limon','amarillo') 
print(c2)
print(custom)

c2.make_juice(4)
custom.make_juice(9)

