number=[1,2,34,56,78,9,8,76,45,44,66,24,44,74,56]
count =0
for i in number:
    if (i%2 ==0):
        print("even number is:", i)
        count+=1
print("total even number is:", count)        