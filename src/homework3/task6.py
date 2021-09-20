'''Упорядоченный список.
    Дан список целых чисел.
    Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок,
    а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
    задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.
'''

str_ = input('Введите список целых чисел: ')
lst = [int(_) for _ in str_.split()]
new, new1 = [], []
for elem in lst:
    if elem:
        new.append(elem)
    else:
        new1.append(elem)
print(new + new1)
