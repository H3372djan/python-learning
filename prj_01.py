import random
class Arthmetic:
    def add (a,b):
        result = a+b
        return result

    def subtract (a,b):
        result = a-b
        return result

    def multipy (x,y):
        result = x*y
        return result

    def divide (w,v):
        result = w/v
        return result

    def reminder (w,v):
        result = w%v
        return result

    def percentage (m,t):
        result = m*100/t
        return result
    def hello (n):
        print(f"hello and welcome {n}")
    def check(q,a):
        if q == a:
            print("Correct")
            return 10
        else:
            print("Incorrect")
            return 0
        
Total_Points = 0

arth = Arthmetic
name = input("Enter your name : ")
max_Question = int(input("Question #: "))
arth.hello(name)
for i in range (0,max_Question):
    r1 = random.randint(1,11)
    r2 = random.randint(1,11)
    op = random.randint(1,3)

    if op == 1:
        result = arth.add(r1,r2)
        q=int(input(f" {r1} + {r2} =   "))
        points=arth.check(q,result)
    elif op == 2:
        result = arth.subtract(r1,r2)
        q=int(input(f" {r1} - {r2} =  "))
        points=arth.check(q,result)
    elif op == 3:
        result = arth.multipy(r1,r2)
        q=int(input(f" {r1} x {r2} =  "))
        points=arth.check(q,result)
    elif op == 4:
        result = arth.divide(r1,r2)
        q=int(input(f" {r1} / {r2} =  "))
        points=arth.check(q,result)
    print(f"--- You got {points} ---")
    Total_Points = Total_Points + points
print(f"Your Total Points = {Total_Points}")        