''' Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета. '''

number = int (input("Input six-digit number ticket: "))
sumLeft = 0
sumRight = 0

while number > 1000:
    sumRight = sumRight + number % 10
    number = number // 10
    

while number > 0:
    sumLeft = sumLeft + number % 10
    number = number // 10


if sumLeft == sumRight :
    print("Wow! Your ticket turned out to be lucky!")
else:
    print("Your regular ticket!")