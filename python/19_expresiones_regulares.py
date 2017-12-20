import re

phone = '605403756 #esto es un coentario'
number = re.sub(r'#.*$','',phone)
print(number)

number =  re.sub(r'\D','',phone)
print('Teléfono')