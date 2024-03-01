continua='S'
while (continua!='N'):
    print("Operação Adição!:")
    numero1=int(input("Digite um valor: "))
    numero2=int(input("Digite um valor: "))
    print(f"{numero1} + {numero2} = {numero1+numero2}")
    continua=str(input("Deseja fazer mais uma soma? [S OU N] "))