"""
Задача 26:  
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
"""

# def stepen(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * stepen(a, b - 1)
    
def stepen(a, b):
    return 1 if b == 0 else stepen(a, b - 1) * a
    
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(stepen(a, b))