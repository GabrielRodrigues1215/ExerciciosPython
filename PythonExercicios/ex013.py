print('SALARIO COM AUMENTO')
s = float(input('Digite seu salario: '))
a = s*0.15 #Ou (a = s * 15/100)
sa = s + a
print ('seu salario é: {}\nO aumento que ira receber é de 15%: {:.2f}\nSeu salario com aumento irá ficar: {:.2f}'.format(s,a,sa))
#CORRIGIDO