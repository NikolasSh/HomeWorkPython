
'''
Дана строка (возможно, пустая), состоящая из букв
A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст
строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная
строка. Пояснения: Если символ встречается 1 раз,
он остается без изменений;
Если символ повторяется более 1 раза,
к нему добавляется количество повторений
'''

string = "BbbbbAAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBCcccc"

def rle_coding(string):
    string = string.upper()
    intermediate_string = ""
    counter_symbol = 1
    compressed_string = ""
    length_str = int(len(string))
    for i in range(length_str):
        if i < length_str-1:
            if string[i] == string[i+1]:
                counter_symbol += 1

                intermediate_string = string[i] + str(counter_symbol)

                if i == length_str-2:
                    compressed_string = compressed_string + intermediate_string


            elif string[i] != string[i+1]:
                counter_symbol = 1
                compressed_string = compressed_string + intermediate_string
                intermediate_string = ""
                if i == 0:
                    compressed_string = compressed_string+ string[0]

                if i < length_str-2:
                    if string[i+1] != string[i+2]:
                        compressed_string = compressed_string + string[i+1]
                if i == length_str-2:
                    compressed_string = compressed_string + string[i+1]
    return compressed_string

result = rle_coding(string)
print(string)
print(result)