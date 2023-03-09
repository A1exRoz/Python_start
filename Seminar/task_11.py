# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# ВАРИАНТ 1
# A = int(input('A = '))
# a1 = 0
# a2 = 1
# last_a = a1 + a2
# i = 2

# while last_a < A:
#     last_a = a1 + a2
#     a1 = a2
#     a2 = last_a
#     i += 1
#     if last_a > A:
#         i = -1
# print(i)

# ВАРИАНТ 2
A = int(input('A = '))
a1, a2 = 0, 1
i = 2

while last_a < A:
    last_a = a1 + a2
    a1 = a2
    a2 = last_a
    i += 1
    if last_a > A:
        i = -1
print(i)