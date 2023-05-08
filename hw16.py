
'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
import random

array = []

def fillArray(array):
    amount_elements = int(input("Input amount elements of array: "))

    for i in range(amount_elements):
        array.append(random.randint(1, 100))

    return array

array_first = fillArray(array)
print(array_first)

def maxMinArrayElement(array):
    min_element = int(input("Input min elements of array: "))
    max_element = int(input("Input max elements of array: "))
    result_array = []
    for i in range(len(array)):
        if min_element <= array[i] <= max_element:
            result_array.append(array[i])

    return result_array

print(maxMinArrayElement(array_first))