# Get the Input string
from collections import Counter
k=input("str: ")

# Sort the string

k=sorted(k)
# Take empty List
l=[]

# For each character in the input
k=Counter(k)

# check whether printed or not
for i in k:
	print("'"+str(i)+f"'\t{k[i]}")

# print char and count
print(list(k))

# add to printed list