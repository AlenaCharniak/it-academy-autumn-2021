''' List practice
    1.Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
'''

lst1 = [''.join([i, k]) for i in 'ab' for k in 'bcd']
print('1: ', lst1)


'''2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
'''

lst2 = slice(0, 6, 2)
print('2: ', lst1[lst2])


''' 3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
'''

lst3 = [str(x) + 'a' for x in range(1, 5)]
print('3: ', lst3)


''' 4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
'''

print('4: ', lst3.pop(1))


''' 5. Скопируйте список и добавьте в него элемент '2a' так, чтобы в исходном списке 
    этого элемента не было.
'''

lst3.insert(1, '2a')
print('5: ', lst3)
