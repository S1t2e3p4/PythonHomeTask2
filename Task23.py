# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system('cls')

num = int(input('Введите число равное размеру списка: '))
number = 1

print('{', end=' ')
for i in range(num):
    if i < num-1:
        number = round((1+1/(i+1))**(i+1), 2)
        print(f'{i+1}: {number}, ', end=' ')
    if i == num-1:
        number = round((1+1/(i+1))**(i+1), 2)
        print(f'{i+1}: {number}', '}')

# По биномиальной формуле <3
