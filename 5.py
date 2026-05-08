#Crie um programa que receba duas notas (0 a 10) e calcule a média.

#Classifique:
#Média ≥ 7  "Aprovado"
#Média entre 5 e 6.9  "Recuperação"
#Média < 5  "Reprovado"


#Restrições:
#A média deve ser armazenada em uma variável
#Use obrigatoriamente elif
#Não pode repetir cálculos diretamente no if

N1 = int(input())
N2 = int(input())

NMedia = (N1 + N2) / 2

if NMedia >= 7:
    print('Aprovado')
elif NMedia >= 5 and NMedia <= 6.9:
    print('Recuperação')
else:
    print('Reprovado')