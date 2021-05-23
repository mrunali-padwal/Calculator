#Addition
def add(x,y):
    print("The addition is : ", x+y)

def subtract(x,y):
    print("The difference is : ",x-y)

def division(x,y):
    if(y != 0):
        print("The division is : ",x/y)
    elif(y == 0):
        print("Divide by zero condition")

def multiply(x,y):
    print("The result of multiplication is : ",x*y)

a = int(input("Enter a first number :" ))
b = int(input("Enter a second number : "))
print("Which operation do you want to perform ?\n 1.Addition\n 2.Subtraction\n 3.Division\n 4.Multiplication\n")
choice = int(input("Enter your choice number : "))
if(choice == 1):
    add(a,b)
elif(choice == 2):
    subtract(a,b)
elif(choice == 3):
    division(a,b)
elif(choice == 4):
    multiply(a,b)
    
