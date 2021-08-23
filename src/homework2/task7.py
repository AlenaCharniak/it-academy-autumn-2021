''' Даны: три стороны треугольника.
    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.
'''

a = int(input('Введите сторону треугольника, a='))
b = int(input('Введите сторону треугольника, b='))
c = int(input('Введите сторону треугольника, c='))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if a + b > c and b + c > a and a + c > b:
    print('Площадь треугольника:', round(s, 2))
else:
    print('Неверные данные')