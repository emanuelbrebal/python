lista=[]
soma=0
numero=int(input("Digite um número. 0 cancela. "))
while (numero!=0):
    soma+=numero
    lista.append(numero)
    numero=int(input("Digite um número. 0 cancela. "))

print("Lista de termos inseridos:", lista)
print("Maior termo inserido:", max(lista))
print("Menor termo inserido:", min(lista))
print("Soma dos termos inseridos:", soma)
