# print all characters of the string

text = input("enter your text:")
count =0
for char in text:
    if char.lower() in "aeiou":
        count+=1
print("number of vowel is:", count)
