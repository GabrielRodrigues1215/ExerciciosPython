import random

aluno1 = input("digite o nome de um aluno: ")
aluno2 = input('digite o nome de outro aluno: ')
aluno3 = input('digite o nome de outro aluno ')
aluno4 = input('digite o nome de outro aluno ')
sorte = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choice(sorte)
print("o aluno sorteado foi {}".format(sorteado))
#Corrigido