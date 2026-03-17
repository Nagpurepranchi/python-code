# Print the elements in the list that appear only once.
a=[1,2,3,4,5,5,6,7,8,9,8,7,6,5,4,3,2,2,9,10,11,24]
unique= set(a)
for i in unique:
    if a.count(i)==1:
        print(i)
        
    
    