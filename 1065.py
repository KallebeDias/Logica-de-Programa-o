par = 0

for Numero in range(5):
    Numero = int(input())
    if((Numero % 2) == 0):
        par += 1

print(f'{par} valores pares')