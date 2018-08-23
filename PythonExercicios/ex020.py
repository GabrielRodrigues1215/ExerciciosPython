import random

aluno1 = input("digite o nome de um aluno: ")
aluno2 = input('digite o nome de outro aluno: ')
aluno3 = input('digite o nome de outro aluno ')
aluno4 = input('digite o nome de outro aluno ')
lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print("a ordem de apresentação será ")
print(lista)
#Corrigido


#outra maneira de fazer
#for i in range (len(lista)):
#    random_index = random.randrange(len(lista))
#    print(lista[random_index])
#    del lista[random_index]
