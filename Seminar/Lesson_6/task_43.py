"""43. Дан список чисел. Посчитайте, сколько в нем пар элементов, 
равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках."""


# Вариант 1
numbers = [1, 2, 3, 2, 2, 2, 3]
count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            count += 1
print(count)