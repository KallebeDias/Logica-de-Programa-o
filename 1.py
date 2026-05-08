#Crie um programa que receba um número inteiro e: Informe se ele é:
#Positivo par
#Positivo ímpar
#Negativo
#Zero

#Restrições:
#Você deve usar if, elif e else
#Deve usar operador lógico (and ou or)
#Não pode usar funções prontas além de input e print

numero = int(input())

if numero > 0 and numero % 2 == 0:
    print("Positivo par")

elif numero > 0 and numero % 2 != 0:
    print("Positivo ímpar")

elif numero < 0:
    print("Negativo")

else:
    print("Zero")