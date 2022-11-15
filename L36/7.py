a=list(map(int,input('data: ').split(',')))
b=[a[i] for i in range(len(a)) if i%2!=0]
print('odd index elements:',b)