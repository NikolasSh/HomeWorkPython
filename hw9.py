'''
Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

import random

N = int(input("Введите количество элементов в массиве: "))
A = []
x = int(random.randint(1, 10))
close_element = 0
min_number = 0
max_number = 0

for i in range(N):
    A.append(i+1)
    close_element = A[i]
    if close_element + 1 == x:
        min_number = close_element
    if close_element - 1 == x:
        max_number = close_element

print(A)
print(x)
print(f"Ближайшие числа в списке A к числу {x} равны {min_number} и {max_number}")