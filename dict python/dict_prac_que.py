# dictionary
"""Dictionary in Python is a data structure in which data is stored in key-value pairs. It means, every value has a unique key through which that value is accessed."""
# They are written in curly braces { }.
# Data is in the key:value format.
# Keys are unique (cannot be repeated).
# Values ​​can be repeated.
# Dictionaries are mutable (can be changed).

# create dict
"""info={
    "key": "value",
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print(info)"""

# to access value
"""info={
    "key": "value",
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print("name:",info["name"])
print("age:",info["age"])
print("subject:",info["subject"])
"""

# to change value 
"""info={
    "key": "value",
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
info["name"]="preet"
print(info)"""

# to add new value
"""info={
    "key": "value",
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
info["surname"]= "nagpure"
print(info)"""

# nested dictionary
"""A nested dictionary means a dictionary within a dictionary.
This means that the value of a dictionary can also be a dictionary."""
#  create dict
"""students={
    "s1":{"name":"pranchi",
          "surname": "nagpure",
          "class": "12th",
          "subject":{"hindi":91,
                     "english":89,
                     "political science": 87,
                     "geography": 90,
                     "socialogy":97,
                     "cs":93}
                     },

    "s2":{"name":"preeti",
          "surname": "nagpure",
          "class": "12th",
          "subject":{"hindi":87,
                     "english":89,
                     "political science": 88,
                     "geography": 91,
                     "socialogy":94,
                     "cs":92}
                     },
}

print("student details:", students)
"""

# value access
"""students={
    "s1":{"name":"pranchi",
          "surname": "nagpure",
          "class": "12th",
          "subject":{"hindi":91,
                     "english":89,
                     "political science": 87,
                     "geography": 90,
                     "socialogy":97,
                     "cs":93}
                     },

    "s2":{"name":"preeti",
          "surname": "nagpure",
          "class": "12th",
          "subject":{"hindi":87,
                     "english":89,
                     "political science": 88,
                     "geography": 91,
                     "socialogy":94,
                     "cs":92}
                     },
}

print("student subject:", students ["s1"]["subject"])

"""
# add new value
"""students={
    "s1":{"name":"pranchi",
          "surname": "nagpure",
          "class": "12th",
          "subject":{"hindi":91,
                     "english":89,
                     "political science": 87,
                     "geography": 90,
                     "socialogy":97,
                     "cs":93}
                     },

    "s2":{"name":"preeti",
          "surname": "nagpure",
          "class": "12th",
          "subject":{"hindi":87,
                     "english":89,
                     "political science": 88,
                     "geography": 91,
                     "socialogy":94,
                     "cs":92}
                     },
}
students["s1"]["grade"]= "A"

print("student details:", students ["s1"])"""

# dictionary method mostly used
# keys
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print(info.keys())
"""

# values
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print(info.values())"""

# items
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print(info.items())"""

# get
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print("name:",info.get("name"))"""

# update
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
info.update({"city":"bhopal"})
print(info)"""

# multiple function
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
print(len(list(info.keys())))
print(info)
"""

# If the dictionary is to be accessed through the index, then the dictionary must be converted into a list.
"""info={
    "name": "pranchi",
    "age" : 21,
    "marks" : 98.4,
    "subject": "python"
}
pairs = list (info.items())
print(pairs[0])
"""

                                     
                                     # practics questions
#  Given a dictionary. Swap the keys and values.
"""dic={
    "a":1,
    "b":2,
    "c":3
}
swap = {k:v  for v,k in dic.items()}
print(swap)            """    

# Find the highest subject mark in student  dictionary.
"""student={
    "name":"pranchi",
    "surname":"nagpure",
    "class": "12th",
    "subjectmark":{"hindi": 95,
                  "english":90,
                  "cs":95,
                  "agriculture":98}
}

top_subject= max(student["subjectmark"], key=student["subjectmark"].get)

print("student hightest mark subject:",top_subject)
print("highest mark:", student["subjectmark"][top_subject])"""


# Find the lowest number input by the user in the dictionary.
"""number={}
n = int(input("How many numbers you want to enter:"))
for i in range(n):
    key= input("enter your key:")
    value =int(input("enter your value:"))
    number[key]= value
lowestnumber = min(number.values())
print("lowestnumber is:", lowestnumber)"""


# Sum up all the values ​​in a dictionary.
"""subjecctmarks={
                 "hindi": 95,
                  "english":90,
                  "cs":95,
                  "agriculture":98
}
totalmark = sum (subjecctmarks.values())
print("total subject mark is:",totalmark)"""


# Find the highest value in a dictionary
"""subjecctmarks={
                 "hindi": 95,
                  "english":90,
                  "cs":95,
                  "agriculture":98
}
totalmark = max (subjecctmarks.values())
print("highest subject mark is:",totalmark)"""


# Calculate the average in a dictionary.
"""subject={
                 "hindi": 95,
                  "english":90,
                  "cs":95,
                  "agriculture":98
}
totalmark = sum (subject.values())
average= totalmark/ len(subject)
print("average mark:", average)
"""

# Convert a dictionary to a list of tuples
"""familyname={
    "fathername":"mr.niteen",
    "mothername":"mrs.preet",
    "daughtername":"miss daisy",
    "sonname":"daahh"
}
print(list(familyname.items()))"""


# Check whether a specific key exists in the dictionary or not

"""familyname={
    "fathername":"mr.niteen",
    "mothername":"mrs.preet",
    "daughtername":"miss daisy",
    "sonname":"daahh"
}
key = input("enter your key to check:")
if key in familyname:
    print("key is exist")
else:
    print("key is not exist")"""

# merge two dictionaries
"""familyname1={
    "fathername":"mr.niteen",
    "mothername":"mrs.preet",
    "daughtername":"miss daisy",
    "sonname":"daahh"
}
familyname2={
    "grandfathername":"mr.nk",
    "grandmothername":"mrs.suu",
    "sisterinlaw":"miss swii",
    "brotherinlaw":"mr.abhi"
}

familyname1.update(familyname2)
print("familyname is:",familyname1)
"""



