# two mandatory parts 1.base case (which stops the loop) 2.recursive case (where the function calls itself)

#example
def number(n):
    if n==0:
        print("Done!")
        return
    print(n)
    number(n-1)
number(5)

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#using loop
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
    
print(fact(5))

#fibonacci

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(8))

#palindrome 

def is_pald(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_pald(s[1:-1])
print(is_pald("madam"))