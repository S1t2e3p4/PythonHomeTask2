# Реализуйте алгоритм перемешивания списка.

import os
import random
os.system('cls')

import os
import random
os.system('cls')

n = int(input('Введите число N: '))

my_list = []
for _ in range(n):
    my_list.append(random.randint(-n, n))
print('Полученный список из N-элементов:', my_list)
random.shuffle(my_list)
print('Переменный случайным образом список из N-элементов:', my_list)
