mylist = [4,5,10,20,10,54,22,1,20]

# 1. Get the lowest value
# 2. Get the highest value
# 3. Print a list of duplicates
# do not use min and max

min = mylist[0]
max = mylist[0]

for a in mylist:
    if a < min:
        min = a

for b in mylist:
    if b > max:
        max = b

print(min)
print(max)


