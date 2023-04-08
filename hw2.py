'''Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?'''

numberCrane = int (input("Enter the number of cranes multiple 6 : "))

cranesPiter = int (numberCrane / 6)
cranesSergey = int (cranesPiter)
cranesKate = int ((cranesPiter + cranesSergey) * 2)

cranesKate 
if numberCrane % 6 != 0:
    print("Attention! Invalid value entered!")
else:
    print(f"Kate collected {cranesKate} cranes, Sergey collected {cranesSergey} cranes, Piter collected {cranesPiter} cranes.")
