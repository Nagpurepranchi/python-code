number={}
n = int(input("How many numbers you want to enter:"))
for i in range(n):
    key= input("enter your key:")
    value =int(input("enter your value:"))
    number[key]= value
lowestnumber = min(number.values())
print("lowestnumber is:", lowestnumber)