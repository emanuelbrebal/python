horario=str(input("Qual turno você estuda?: M-matutino, V-vespertino, N-noturno. "))

if horario=='M' or horario=='m':
        print('Bom dia!')
elif horario=='V' or horario=='v':
        print('Boa tarde!')
elif horario=='N' or horario=='n':
        print('Boa noite!')
else:
    print('Entrada inválida')