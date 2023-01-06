# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system('cls')

num = int(input('Введите число: '))
number = 1

my_list = []
for i in range(num):
    number *= (i + 1)
    my_list.append(number)

print('[', end='')
print(*my_list, sep=', ', end='')
print(']', end='')