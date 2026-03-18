# Count vowels and consonants in a string
text =input("enter a text or para:")
vowel=0
constant=0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel+=1
        else:
            constant+=1
print("vowel is:", vowel)
print("constant is:",constant)