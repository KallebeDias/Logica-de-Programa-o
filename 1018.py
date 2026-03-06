Valor = int(input())

Cedulas = [100, 50, 20, 10, 5, 2, 1]

print(Valor)

for nota in Cedulas:
    quantidade = Valor//nota
    Valor = Valor%nota

    print(f'{quantidade} nota(s) de R$:{nota},00')