respostaPositiva='sSsimSim'
respostaNegativa='nNnaoNaonãoNão'
contadorPositiva=0
print("--Interrogatório--")

resposta1=str("Você, por um acaso, telefonou para a vítima?")

if resposta1 in respostaPositiva:
        contadorPositiva+=1
elif respostaNegativa:
        contadorPositiva=contadorPositiva
else: 
        print("Resposta Inválida e não contabilizada")

resposta2=str("Você, por um acaso, esteve no local do crime?")
if resposta2 in respostaPositiva:
        contadorPositiva+=1
elif respostaNegativa:
        contadorPositiva=contadorPositiva
else: 
        print("Resposta Inválida e não contabilizada")        

resposta3=str("Você, por um acaso, mora perto da vítima?")
if resposta3 in respostaPositiva:
        contadorPositiva+=1
elif respostaNegativa:
        contadorPositiva=contadorPositiva
else: 
        print("Resposta Inválida e não contabilizada")
        
resposta4=str("Você, por um acaso, devia para a vítima?")
if resposta4 in respostaPositiva:
        contadorPositiva+=1
elif respostaNegativa:
        contadorPositiva=contadorPositiva
else: 
        print("Resposta Inválida e não contabilizada")
        
resposta5=str("Você, por um acaso, já trabalhou com a vítima?")
if resposta5 in respostaPositiva:
        contadorPositiva+=1
elif respostaNegativa:
        contadorPositiva=contadorPositiva
else: 
        print("Resposta Inválida e não contabilizada")
        
        
if contadorPositiva==2:
        print("Suspeito")
elif contadorPositiva>=3 or contadorPositiva==4:   
        print("Cúmplice")
elif contadorPositiva>5:
        print("Assassino")
else: 
        print("Inocente")