'''Напишите программу, которая считает общую цену.
   Вводится M рублей и N копеек цена, а также количество S товара.
   Посчитайте общую цену в рублях и копейках за L товаров.
   
   Пример:
   Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
   Output: Общая цена 9 рублей 60 копеек
'''

cena = float(input('Введите стоимость: '))
tovar = int(input('Введите количество товара: '))
stoim = cena*tovar
print("Общая цена: ", int(stoim//1), 'руб.', int(round(stoim%1,2)*100), 'коп.')