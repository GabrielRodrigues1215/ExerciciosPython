import math
an = float(input('digite um angulo: '))
cosseno = math.cos(math.radians(an))
seno = math.sin(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an,cosseno))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an,seno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an,tangente))
#Corrigido