#  Given a dictionary. Swap the keys and values.
dic={
    "a":1,
    "b":2,
    "c":3
}
swap = {k:v  for v,k in dic.items()}
print(swap)            