from main import  get_result

import sys

menu= int(input("Menu\n=======\n1) Character\n2). Word\n:"))

if menu ==1:
  char=input('Ingrese un caracter:')
  word = char
elif menu==2:
  word= input('Ingrese una palabra:')

else:
  sys.exit()

print('====================\nResults\n====================')

results= get_result(word)
print('Total {0}'.format(results))