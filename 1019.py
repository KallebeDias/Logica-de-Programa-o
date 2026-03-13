segundos = int(input())

Horas = Segundos//3600 
Segundos = Segundos%3600 
Minutos = Segundos//60
Segundos = Segundos%60

print(f'{Horas}:{Minutos}:{Segundos}')