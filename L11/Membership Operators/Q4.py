# Program to illustrate membership
L1 = ['A', '123', 'Ramana', [1, 2], 34.56, '55']
# for 34.56 returns False as output because input() return type is True so it converts 34.56 as string.
print(L1)
elem=input("element: ")
# write your code here
print(f'{elem} in {L1} is: {elem in L1}')
print(f'{elem} not in {L1} is: {elem not in L1}')