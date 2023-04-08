'''Требуется определить, можно ли от шоколадки размером 
n × m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
'''

numberSlicesWidth = int(input("Enter the number of slices by width: "))
numberSlicesLength = int(input("Enter the number of slices in length: "))
numberSlicesBreak = int(input("Enter how many slices do you want to break off: "))

if numberSlicesBreak > numberSlicesWidth * numberSlicesLength:
    print("Incorrect number of broken slices entered!")
    exit ()

if numberSlicesBreak == numberSlicesWidth * numberSlicesLength:
    print("In this case, you won't break anything!")
    exit ()

if numberSlicesBreak % numberSlicesWidth == 0 or numberSlicesBreak % numberSlicesLength == 0:
    print("You can divide the chocolate bar into two rectangles!")

else:
    print("You can't split a chocolate bar into two rectangles!")