# list 
"""List in Python is a data structure in which we can store multiple values ​​in a single variable.
List is written within square brackets [] and elements are separated by comma."""

"""marks= [34.5,56.5,67,56,]
print (marks)
print(marks[0])
print(len(marks))"""

"""studentdetails= ["pranchi", 98.67, "bhopal"]
print(studentdetails)
studentdetails[0]= "preet"
print(studentdetails)
print( studentdetails[-3:-1])"""

"""number = [2,3,5,4,1,6,8,7,9]
print(number)
number.append(10)
print("after append:", number)
number.insert(0,0)
print("after insert:", number)
number.remove(9)
print("after remove:", number)
number.pop()
print("after pop:", number)
number.sort()
print("after sort:", number)
number.reverse()
print("after reverse:", number)"""

"""
fruitename= ["banana","orange","mango","apple","litchi","papaya"]
print("fruitename:", fruitename)
fruitename.append("grapes")
print("after add fruite name:", fruitename)
fruitename.remove("mango")
print("after remove fruite:", fruitename)
fruitename.sort()
print("after accessnding order:",fruitename)
fruitename.reverse()
print("after reversing:", fruitename)
"""
                                # practics question

# Create a list of 5 numbers and print it.
"""number= [1,2,3,4,5]
print(number)"""

# Write a program to add an element to a list using append()
"""familytlist= ["pranchi","priti", "mitalee","nitya"]
print("before append:",familytlist)
familytlist.append("dhanula")
print("after appends:", familytlist)"""

# Write a program to add an element to a list using extend()
"""familytlist= ["pranchi","priti", "mitalee","nitya"]
print("before extend:",familytlist)
familytlist.extend(["dhanula", "vinod"])
print("after extend:", familytlist)
"""

# Create a list of fruits and remove one fruit using remove()
"""fruitsname=["banana","apple","mango","grapes","papay"]
print("before remove fruits:",fruitsname)
fruitsname.remove("apple")
print("after remove fruits:",fruitsname)"""


# Write a program to sort a list in ascending order
"""numbers=[2,4,6,8,10,1,3,5,7,9]
print("List before sorting:",numbers)
numbers.sort()
print("List after sorting:",numbers)"""


# Write a program to reverse a list.
"""numbers=[2,3,1,4,6,5,7,9,8,10]
print("List before reverse:",numbers)
numbers.reverse()
print("List after reverse:",numbers)
"""

# Write a program to print the first and last element of a list.
"""studentname=["pranchi","preet","niteen","nk"]
print("first element:",studentname[0])
print("last element:",studentname[-1])"""


# write a program to count how many times a number appears in a list.
"""num=[1,2,3,4,5,6,3,2,1,4,5,6,7,4]"""
# print(num.count(1))
"""for i in[1,2,3,4,5,6,3,2,1,4,5,6,7,4]:
    print(i,"comes",num.count(i),"num")
"""

# Write a Python program to remove duplicates from a list
"""name=["pranchi","nk","niteen","niteen"]
print("list before remove duplicate items:", name)
name= list(set(name))
print("List after removing duplicates:",name)
"""

# Given a list of integers, write a function to find the largest number.
"""num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
num3=int(input("enter your third number:"))
num4=int(input("enter your fourth number:"))
if(num1>num2 and num1>num3 and num1>num4):
    print("largest number is:",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("largest number is:", num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("largest number is:", num3) 
elif(num4>num1 and num4>num2 and num4>num3):
    print("largest number is:", num4)     """


# How would you merge two lists into a single sorted list?
"""list1=[1,2,3,4,5]
list2=[6,7,8,9,10,11]
merged=list1 + list2
merged.sort
print("merged and sort list:",merged)"""


# tuples
"""A tuple is a collection of elements in Python that is ordered and immutable (cannot be changed).
Tuples are written using parentheses () and can store different types of data."""

# Create a tuple of 5 numbers and print it
"""number=(1,2,3,4,5)
print(number)"""

# Write a program to find the index of an element in a tuple.
"""para=("i am pranchi nagpure","i am learning python","for devops")
print(para[2])
"""

# Write a program to count occurrences of a number in a tuple.
"""tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
num=int(input(" Enter the number you want to count from the tuple:"))
count = tuple.count(num)
print("the number",num, "occurres",count ,"of the tuple")"""


# Write a program to print the second element of a tuple.
"""tuple=(1,2,3,4,5,6,7,8)
print(tuple[1])"""

# Write a Python program to create a tuple of squares of numbers from 1 to 5
"""print(1*1)
print(2*2)
print(3*3)
print(4*4)
print(5*5)"""
        #   with for loop
"""for i in range(1,6):
    squre= i*i
    print("squre of",i,"this",squre,)
"""

# Given a tuple of integers, write a function to find the sum of all elements.

"""def sum_tuple(t):
    total = 0
    for i in t:
        total = total + i
    return total
number = (1,2,3,4,5,6,7,8)
result = sum_tuple(number)
print("sum of the numbers:", result)"""

# How would you unpack a tuple of values into separate variables?
"""tuple=(1,2,3,4,5)
a,b,c,d,e = tuple
print("Storing the elements of a tuple in separate variables.",a)
print("Storing the elements of a tuple in separate variables.",b)
print("Storing the elements of a tuple in separate variables.",c)
print("Storing the elements of a tuple in separate variables.",d)
print("Storing the elements of a tuple in separate variables.",e)"""



                    # combine question
# Write a program to convert a list into a tuple.
# create list
"""studentlist=["pranchi","niteen","preet","nk"] 
print("before:",studentlist)
# convert into tuple
studenttuple = tuple(studentlist)  
print("tuple:",studenttuple)  
           """


# Write a Python program to find the common elements between a list and a tuple.
"""mylist =[1,2,3,4,5,6,7,8,9,10,11]
tuple=(1,2,3,4,5,6,7,8)
common_element= list(set(mylist) & set(tuple))
print("commom element of the list and tuple:", common_element)
"""

# Given a string, write a code to convert it into a list of words
# When we break a string into words and store it in a list, it is called converting string into a list of words.
"""sentence="I am currently learning Python because I want to build a strong foundation for DevOps. By understanding Python thoroughly, I can manage automation, scripting, and various tasks more efficiently in DevOps. My goal is to learn it step by step, so I can apply the concepts correctly and solve problems effectively. This way, I will have a solid base to work with DevOps tools and practices confidently."
words= sentence.split()
print(words)"""

#  How would you concatenate a list of strings into a single string with a specified separator?
"""words= ["python","is", "a", "very", "easy", "programming", "language"]
sentence = "  " .join(words)
print(sentence)
""" 
        #    by comma
"""words= ["python","is", "a", "very", "easy", "programming", "language"]
sentence = " , " .join(words)
print(sentence)"""

                   #  by hyphen
"""words= ["python","is", "a", "very", "easy", "programming", "language"]
sentence = " - " .join(words)
print(sentence)                    
"""



# Write a program to print elements of a list using slicing.
"""list = [1,2,3,4,5,6,7,8,9,10,11,12]
print("first three numbers:", list[:3])
print("last fourth number:", list[-5:-1])
print("mid number:",list[4:7])
print("all number:",list)"""