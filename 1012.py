A, B, C = map(float, input().split())
pi = 3.14159

Triangulo = A * C /2
Circulo = C**2 * pi
Trapezio = (A + B) * C / 2
Quadrado = B**2
Retangulo = A * B
print(f'TRIANGULO: {Triangulo:.2f}')
print(f'Circulo: {Circulo:.2f}')
print(f'Trapezio: {Trapezio:.2f}')
print(f'Quadrado: {Quadrado:.2f}')
print(f'Retangulo: {Retangulo:.2f}')