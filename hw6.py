"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
import random


x = int(random.randint(1, 1001))
y = int(random.randint(1, 1001))

print(x, y)

s = x + y
p = x * y

print(s, p)

x1 = ((s*x) - p) ** (0.5)
x1 = int(x1)
y1 = s - x

print(x1,y1)




