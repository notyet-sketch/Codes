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
    if a<0:
        raise ValueError("Can't square root a nagetive number.")
    return math.sqrt(a)

def modulus(a,b):
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a%b

def get_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def show_menu():
    print("\n========== Modular Calculator ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Exit")

def calculator():

    operators={
        "1":add,
        "2":subtract,
        "3":multiply,
        "4":divide,
        "5":power,
        "6":modulus,
    }

    while True:
        show_menu()
        choice=input("Enter your choice (1-8) : ")
        
        if choice=="8":
            print("Thanks for using the calculator.")
            break
        
        try:
            if choice in operators:
                num1=get_num("Entet first number : ")
                num2=get_num("Enter second number : ")
                result= operators[choice](num1,num2)
                print("Result : ",result)
            elif choice=="7":
                num=get_num("Enter number : ")
                result= root(num)
                print(f"Result : {result:0.4f}")
            else:
                print("Invalid choice. Please try (1-8).")

        except ValueError as e:
            print("Error : ",e)

if __name__ == "__main__":
    calculator()