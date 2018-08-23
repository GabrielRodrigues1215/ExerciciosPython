print('ALUGUEL DE CARRO')
d = int(input("quantos dias o carro foi alugado: "))
k = float(input('quantidade de quilometros percoridos: '))
cd = d * 60
ck = k * 0.15
total= cd + ck
print('O total a pagar é de R${}'.format(total))
#CORRIGIDO