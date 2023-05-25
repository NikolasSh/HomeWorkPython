'''
 Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
 Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной

1.Функция на ввод данных - готово
2.Функция на вывод данных - готово
3.Функция по поиску и выводу характеристик - готово
4.Запуск нужной функции - готово

'''
def input_data():
    surname = input("Enter your surname, please: ")
    name = input("Enter your name, please: ")
    patronymic = input("Enter your patronymic, please: ")
    phoneNumber = input("Enter your phone number, please: ")
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(surname + " " + name + " " + patronymic + " " + phoneNumber + '\n')

def search_data():
    search = input("Enter search parameter, please(name, surname, patronymic, phone): ")
    search_result = list()
    if search == "name":
        with open("phonebook.txt", 'r', encoding='utf-8') as file:
            text = list(file.read().split())
            name = input("Enter name, please: ")

            for i in range(len(text)):
                if text[i] == name:
                    search_result.append(text[i-1])
                    search_result.append(text[i])
                    search_result.append(text[i+1])
                    search_result.append(text[i+2])

            if name not in text:
                print("Name not found!!!")



    elif search == "surname":
        with open("phonebook.txt", 'r', encoding='utf-8') as file:
            text = list(file.read().split())
            surname = input("Enter surname, please: ")
            for i in range(len(text)):
                if text[i] == surname:
                    search_result.append(text[i])
                    search_result.append(text[i+1])
                    search_result.append(text[i+2])
                    search_result.append(text[i+3])
            if surname not in text:
                print("Surname not found!!!")

    elif search == "patronymic":
        with open("phonebook.txt", 'r', encoding='utf-8') as file:
            text = list(file.read().split())
            patronymic = input("Enter patronymic, please: ")
            for i in range(len(text)):
                if text[i] == patronymic:
                    search_result.append(text[i-2])
                    search_result.append(text[i-1])
                    search_result.append(text[i])
                    search_result.append(text[i+1])
            if patronymic not in text:
                print("Patronymic not found!!!")

    elif search == "phone":
        with open("phonebook.txt", 'r', encoding='utf-8') as file:
            text = list(file.read().split())
            phone = input("Enter phone number, please: ")
            for i in range(len(text)):
                if text[i] == phone:
                    search_result.append(text[i-3])
                    search_result.append(text[i-2])
                    search_result.append(text[i-1])
                    search_result.append(text[i])
            if phone not in text:
                print("Phone number not found!!!")

    else:
        print("Invalid value entered!!!")
    return print(" ".join(search_result))

def output_data():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)

def data_one():
    operation = input("Enter what you want to do, please(inp, outp, search): ")
    if operation == "inp":
        input_data()
    elif operation == "outp":
        output_data()
    elif operation == "search":
        search_data()
    else:
        print("Invalid value entered!!!")

data_one()
