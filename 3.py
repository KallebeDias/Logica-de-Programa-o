#Crie um programa que receba a idade de uma pessoa.

#Classifique:
#0 a 12  Criança
#13 a 17  Adolescente
#18 a 59  Adulto
#60 ou mais  Idoso
#Se a idade for negativa  "Idade inválida"

#Restrições:
#Deve usar pelo menos um operador and
#Deve tratar erro (idade negativa)
#Estrutura obrigatória com elif

idade = int(input("Digite a idade: "))

if idade < 0:
    print("Idade inválida")

elif idade >= 0 and idade <= 12:
    print("Criança")

elif idade >= 13 and idade <= 17:
    print("Adolescente")

elif idade >= 18 and idade <= 59:
    print("Adulto")

else:
    print("Idoso")