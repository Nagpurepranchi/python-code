# Fibonacci series printed with (n terms)
n= int(input("enter a number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum