""" Напишите программу, которая принимает на вход два числа и проверяет, 
является ли одно число квадратом другого.

*Примеры:*  
- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет """

number_1 = int(input('Введите число а: '))
number_2 = int(input('Введите число b: '))
if number_1 ** 2 == number_2 or number_2 ** 2 == number_1:
    print('yes')
else:
    print('no')