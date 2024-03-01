numeros=[]
numero1=int(input("Digite o primeiro número: "))
numeros.insert(0, numero1)

numero2=int(input("Digite o segundo número: "))
numeros.insert(1, numero2)

numero3=int(input("Digite o terceiro número: "))
numeros.insert(2, numero3)


print("Maior valor digitado: ", max(numeros))