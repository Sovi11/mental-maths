import random 
import time 

def addition_problem(d):
    if d=="E":
        a = random.randint(1,10)
        b = random.randint(1,10)
    if d=="M":
        a = random.randint(10,100)
        b = random.randint(10,100)
    if d=="H":
        a = random.randint(100,1000)
        b = random.randint(100,1000)
    c = int (input(f"What is {a} + {b}\n"))
    if (c==a+b):
        print("Correct")
    else:
        print("Incorrect")

def multiplication_problem(d):
    if d=="E":
        a = random.randint(1,10)
        b = random.randint(1,10)
    if d=="M":
        a = random.randint(1,10)
        b = random.randint(10,100)
    if d=="H":
        a = random.randint(10,100)
        b = random.randint(10,100)
    c = int (input(f"What is {a} x {b}\n"))
    if (c==a*b):
        print("Correct")
    else:
        print("Incorrect")
        
def subtraction_problem(d):
    if d=="E":
        a = random.randint(1,10)
        b = random.randint(1,10)
    if d=="M":
        a = random.randint(10,100)
        b = random.randint(10,100)
    if d=="H":
        a = random.randint(100,1000)
        b = random.randint(100,1000)
    c = int (input(f"What is {a} - {b}\n"))
    if (c==a-b):
        print("Correct")
    else:
        print("Incorrect")
    
mode = input("Which mode do you want to play Addition (A) , Multiplication (M) , Subtraction (S)\n").strip()
diffiulty  = input("select difficulty level Easy (E) , Medium (M) , Hard(H)\n").strip()
count = int(input("How many questions do you want\n"))

while(count > 0) : 
    if (mode == "A"): addition_problem(diffiulty)
    if (mode == "M"): multiplication_problem(diffiulty)
    if (mode == "S"): subtraction_problem(diffiulty)
    count-=1 
