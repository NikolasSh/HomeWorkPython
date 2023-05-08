
"""
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

array = []

def fillArray(array):
    first_number = int(input("Input first number array: "))
    amount_elements = int(input("Input amount elements of array: "))
    difference = int(input("Input difference elements: "))
    for i in range(1, amount_elements+1):
        if i == 1:
            array.append(first_number)
        if i > 1:
            next_element = first_number + (i - 1) * difference
            array.append(next_element)

    return array

print(fillArray(array))