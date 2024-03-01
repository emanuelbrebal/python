numero=int(input("Digite um número: "))

ehPar=numero%2
if ehPar==1:
    print("É ímpar")
elif ehPar==0:
    print("É par")
else:
    print("Erro")