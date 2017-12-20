import time

seconds = time.time()
print('número de ticks desde las 12:00 del 1 de enero de 1970',seconds)

local_time = time.localtime(seconds)

print(local_time)
asctime = time.asctime(local_time)

print(asctime)

date_format ='%d-%m-%Y a las %H:%M:%S'
date_formatted = time.strftime(date_format,time.gmtime(seconds))

print(date_formatted)