# This is my Tossing Coin
import random
for i in range (0,5):
    r = random.randint (1,2)
    a = int (input("Do you want Head = 1 or Tails = 2 : __ "))
    if a == r:
        print("You Won")
    else:
        print("You Lost")    