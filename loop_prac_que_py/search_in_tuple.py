# search for a number x in this tuple using loop {1,4,9,16,25,36,49,64,81,100}
nums= (1,4,9,16,25,36,49,64,81,100)
print("tuple number is:", nums)
x= int(input("enter the number of the tuples:"))
i=0                                             #intilazation
while i<=len(nums):
    if(nums[i]==x):
        print("found at index:",i)
        break
    i+=1
else:
    print("not found")