from math import sqrt
x=int(input())
def isPrime(n):
    if(n<=1):
        print("1")
        return 0;
    if(n==2):
        print("Простое")
        return 1;
    if(n%2==0):
        print("Составное")
        return 0;
    for i in range(2,int(sqrt(n))):
        if n%i==0:
            print("Составное")
            return;
    print("Простое")

isPrime(x)
