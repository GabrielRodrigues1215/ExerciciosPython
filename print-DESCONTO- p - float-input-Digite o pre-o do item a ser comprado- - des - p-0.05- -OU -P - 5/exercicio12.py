print("DESCONTO")
p = float(input('Digite o preço do item a ser comprado: '))
des = p*(0.05) #OU (P * 5/100)
pdes = p - des
print ('um procudo que custa {}\n%5 de desconto neste produto fica {:.2f}\nCom desconto o produto sairá no preço de {:.2f}'.format(p,des,pdes))
#CORRIGIDO
