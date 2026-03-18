# search for a number x in this tuple using Loop
# [1,4,9,16,25,36,49,64,81,100]
nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("enter number: "))
index = 0

for val in nums:
    if val == x:
        print("number found at index:", index)
    index += 1   