# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите сколько долек на первой стороне: "))
m = int(input("Введите сколько долек на второй стороне: "))
k = int(input("Введите сколько хотите отломить: "))

if (k % n == 0 or k % m == 0):
    print(n, m, k, " -> yes")
else:
    print(n, m, k, " -> no")