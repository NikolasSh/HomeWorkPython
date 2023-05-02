'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''



def new_multiplicity():
    n = int(input("Введите количество элементов первого списка: "))
    m = int(input("Введите количество элементов второго списка: "))
    numbers_one = list()
    numbers_two = list()


    for i in range(n):
        numbers_one.append(int(input("Введите элемент первого списка: ")))
    print(numbers_one)

    for j in range(m):
        numbers_two.append(int(input("Введите элемент второго списка: ")))
    print(numbers_two)

    a = set(numbers_one)
    b = set(numbers_two)
    c = a.union(b)
    c = list(c)
    print(c)
    c.sort()
    result_numbers = c

    print(result_numbers)



new_multiplicity()