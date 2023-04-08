#Найдите сумму цифр трехзначного числа. 

i = int (input("Input number: "))
sum = 0

while i > 0 :
    sum = sum + i % 10
    i = i // 10

print(f"The sum of the digits of the entered number is {sum}")