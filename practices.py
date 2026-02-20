#factorial

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

#fibonacci

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(8))

#palindrome

def pal(st):
    if len(st)<=1:
        return True
    if st[0]!=st[-1]:
        return False
    return pal(st[1:-1])
print(pal("madam"))