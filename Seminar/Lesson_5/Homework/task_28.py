"""Задача 28: 
Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

*Пример:*

2 + 2  =  4 
"""

def sum(A, B):
    if B == 0:
        return A
    else:
        return A + sum(A, B - 1)
    
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print(sum(A, B))