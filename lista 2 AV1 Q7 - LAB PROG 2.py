sexo='fFmM'
eCivil='sScCvVdD'

nome=str(input("Digite um nome: "))
if (len(str(nome))<3):
    print("Nome inválido. Deve ter mais que 3 caracteres.")
else:
    print("Nome válido.")

idade=int(input("Digite sua idade: "))
if (idade>0 and idade<150):
    print("Idade válida")
else:
    print("Idade inválida. Deve estar entre 0 e 150 anos.")

salario=int(input("Digite seu salário: "))
if(salario>0):
    print("Salário válido")
else: 
    print("Salário inválido. Deve ser maior que 0.")

sex=str(input("Digite seu sexo: M ou F"))
if sex in sexo:
    print("Sexo válido.")
else: 
    print("Sexo inválido. Opções válidas: M, m, F ou f.")

estadoCivil=str(input("Digite seu estado civil: S - Solteiro(a), C - Casado(a), V - Viuvo(a), D - Divorciado(a)"))
if estadoCivil in eCivil:
    print("Estado Civil Válido.")
else: 
    print("Estado Civil inválido. Opções válidas: S, s, C, c, V, v, D ou d.")
