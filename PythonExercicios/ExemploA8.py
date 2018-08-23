import  math
import emoji #Biblioteca baixada Do Python.org pypi


print(emoji.emojize('Olá, mundo :earth_africa:', use_aliases = True))
num = int (input(' digite um numero: '))
raiz = math.sqrt(num)                         #math.cell = arredonda para baixo
                                              #math.floor = arredonda para cima
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))