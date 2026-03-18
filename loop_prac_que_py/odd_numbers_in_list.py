# Print only odd numbers from the list

number=[1,2,3,4,5,67,89,98,76,45,34,56,23,456,76,89,765,2435,34,56,67,23456,21345,123456]
count= 0
for i in number:
    if(i%2 !=0):
        print("odd number is:", i)
        count+=1

print("total odd number is:", count)        