PREGUNTA = '¿Cómo te llamas?'
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA,'¿Como estas?')

respuesta_formateada = 'Hola {}, ¿Como estas?'.format(RESPUESTA)

print(respuesta_formateada)