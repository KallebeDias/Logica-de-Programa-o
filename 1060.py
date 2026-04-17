Numero = [float(input()) for i in range(6)]

positivos = len([i for i in Numero if i > 0])

print(f'{positivos} Valores positivos')