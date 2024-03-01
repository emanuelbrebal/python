lista=[]
soma=0
numero=int(input("Digite um número entre 0 e 1000. -1 encerra. "))
while (numero!=-1):
    if(numero>=0 and numero<=1000):
        soma+=numero
        lista.append(numero)
        numero=int(input("Digite um número entre 0 e 1000. -1 encerra. "))       
    else:
        numero=int(input("Por favor, tente um número entre 0 e 1000."))
        continue
        

print("Lista de termos inseridos:", lista)
print("Maior termo inserido:", max(lista))
print("Menor termo inserido:", min(lista))
print("Soma dos termos inseridos:", soma)
