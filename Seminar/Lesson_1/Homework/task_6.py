# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


number = input("Введите шестизначное число: ")
while (len(number) != 6):
    print("Вы ввели не верное число, попробуй еще раз: ")
    number = input()
    
if (int(number[0]) + int(number[1]) + int(number[2])) != (int(number[3]) + int(number[4]) + int(number[5])):
# if int((number // 100000) + (number // 10000) + (number // 1000)) != int((number % 10) + (number % 100) + (number % 1000)):
    print(number + " -> no")
else:
    print(number + " -> yes")