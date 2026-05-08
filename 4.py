#Crie um programa que receba três números e:

#Informe o maior número
#Caso todos sejam iguais  "Todos os valores são iguais"
#Caso existam dois maiores iguais, informar o valor e dizer "empate"

#Restrições:
#Deve usar operadores and ou or
#Não pode usar max()
#Deve usar múltiplos elif

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 == n2 and n2 == n3:
    print("Todosos valores são iguais")

elif n1 > n2 and n1 > n3:
    print("Maior número:", n1)

elif n2 > n1 and n2 > n3:
    print("Maior número:", n2)

elif n3 > n1 and n3 > n2:
    print("Maior número:", n3)

elif n1 == n2 and n1 > n3:
    print("Empate entre:", n1)

elif n1 == n3 and n1 > n2:
    print("Empate entre:", n1)

else:
    print("Empate entre:", n2)