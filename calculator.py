import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ValueError("Can't divide by zero.")
    return a/b

def power(a,b):
    return math.pow(a,b)

def root(a):
    return math.sqrt(a)

def modulus(a,b):
    return a%b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Error : ",e)

def show_options():
    print("""
<<<<<<<<<< Modular Calculator >>>>>>>>>>
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. Square Root
8. Exit""")

def calculator():
    operators={
        "1":add,
        "2":subtract,
        "3":multiply,
        "4":divide,
        "5":power,
        "6":modulus
    }
    while True:
        show_options()
        choice=input("Enter choice (1-8) :")
        if choice=="8":
            print("Thanks for using the calculator.")
            break
        try:
            if choice in operators:
                num1=get_number("Enter first number : ")
                num2=get_number("Enter second number : ")
                result=operators[choice](num1,num2)
                print("Result = ",result)
            elif choice=="7":
                num=get_number("Enter number : ")
                result=root(num)
                print(f"Result = {result:0.2f}",)
            else:
                print("Invalid choice. Please try (1-8)")
        except Exception as e:
            print("Error : ",e)

            


if __name__ == "__main__":
    calculator()