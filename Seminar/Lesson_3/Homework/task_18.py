"""
Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – 
количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

numbers = [1, 5, 8, 11, 15]
X = int(input('Введите число: '))
min_step = abs(X - numbers[0])
near_elem = 0

for i in range(1, len(numbers)):
    count = abs(X - numbers[i])
    if count < min_step:
        min_step = count
        near_elem = i
print(numbers[near_elem])


