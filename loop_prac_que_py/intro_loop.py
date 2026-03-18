# A loop is used to run code repeatedly (repeat) until a condition is true or all elements of a collection are covered.
# 2 type of loop
# for loop= It is used when we want to operate on the elements of a list, string, or range one by one.
# syntax
"""for variable in sequence:
    # code block
"""
# example
"""for i in range(1,6):
    print(i)"""


# while loop=The loop will continue as long as the condition remains true.
# syntax
"""while condition:"""
    # code block

    # example
"""i = 1
while i <= 5:
    print(i)
    i += 1"""

"""Important Points:
A loop can be infinite if the condition never becomes false.
break → stops the loop immediately.
continue → skips the current iteration and moves on to the next."""
# example

"""for i in range(1,7):
    if i==3:
        continue
    if i==7:
        break
    print(i)"""


count= 1
while count <=5:
    print("hello")
    count+=1