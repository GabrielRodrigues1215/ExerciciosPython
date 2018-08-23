import math
co = float(input('Digite o comprimento do cateto oposto em metros: '))
ca = float(input('Digite o comprimento do cateto adjacente em metros:  '))
#hipq = (co*co) +(ca*ca)
#hip =  math.sqrt(hipq)
hip = math.hypot(co, ca)
print('valor correto da hipotenusa {}m'.format(hip))