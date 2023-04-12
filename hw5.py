

n = int(input("Input amount coin: "))
amountObverse = int(input("Input amount obverse coin: "))
amountReverse = n - amountObverse

if amountObverse > amountReverse or amountObverse == amountReverse:
    print(f"Minimum number of coins to flip = {amountReverse}")

else : print(f"Minimum number of coins to flip = {amountObverse}")

