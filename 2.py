#Receba uma nota de 0 a 10 e classifique:

#9 a 10  "Excelente" + "Aprovado"
#7 a 8.9  "Bom" + "Aprovado"
#5 a 6.9  "Regular" + "Recuperação"
#Abaixo de 5  "Insuficiente" + "Reprovado"
#Se a nota for inválida (<0 ou >10)  "Nota inválida"

#Restrições:
#Deve usar and em pelo menos uma condição
#Deve usar elif
#Não pode usar estruturas aninhadas (if dentro de if)


nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida")

elif nota >= 9 and nota <= 10:
    print("Excelente")
    print("Aprovado")

elif nota >= 7 and nota < 9:
    print("Bom")
    print("Aprovado")

elif nota >= 5 and nota < 7:
    print("Regular")
    print("Recuperação")

else:
    print("Insuficiente")
    print("Reprovado")