# Factorial Find of a Number(user input)
number= int(input("enter a number to find factorial:"))
fact = 1
for val in range(1,  number+1):
    fact *=val
print("factorial of the number:",fact)    

