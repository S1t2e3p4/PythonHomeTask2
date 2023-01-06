# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
import random
os.system('cls')

n = int(input('Введите число N: '))

my_list = []
for _ in range(n):
    my_list.append(random.randint(-n, n))
print('Полученный список из N-элементов:', my_list)

positions = []
data = open('storepositions.txt', 'w')
position_num = 0
for i in range(n):
        position_num = random.randint(0, n-1)
        data.write((f'{position_num}\n'))
        positions.append(position_num)
data.close()

print()
print('Номера позиций:', positions)

result = 1
for j in range(n):
   result *= my_list[positions[j]]
print()
print(f'Произведение элементов на указанных позициях {positions} = {result}')
