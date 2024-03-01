numero=int(input("Digite um número: "))
i=1
contPrimo=0
while(i<=numero):
    ehPrimo=numero%i
    i+=1
    if(ehPrimo==0):
        contPrimo+=1
    else:
        continue
    

if (contPrimo==2):
    print("Esse número é primo")
else:
    print("Esse número não é primo")