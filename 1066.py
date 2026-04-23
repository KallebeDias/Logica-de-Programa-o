par = 0
impar = 0
positivo = 0
negativo = 0

for Numero in range(5):
    Numero = int(input())
    if((Numero % 2) == 0):
        par += 1
    else:
        impar += 1
    if(Numero > 0):
        positivo += 1
    elif(Numero < 0):
        negativo += 1

print(f'{par} Vaor(es) pare(s)')
print(f'{impar} Vaor(es) impar(es)')
print(f'{positivo} Vaor(es) positivo(s)')
print(f'{negativo} Vaor(es) negativo(s)')