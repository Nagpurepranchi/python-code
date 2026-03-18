# Search number in a list (found/not found)

num =[12,34,56,78,65,76,12,14,35,65,34]
x= int(input("enter a number from the list:"))
found = False
for val in num:
    if val ==x:
        found = True
        break
if found:
       print("found number")   
else:
    print("not found")     