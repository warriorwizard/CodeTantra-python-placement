a=input('data1: ').split(',')
b=input('data2: ').split(',')
dic=dict(sorted(zip(a,b)))
print('before exchange:',list(dic.items()))
di={x:y for y,x in dic.items()}
print('after exchange:',list(sorted(di.items())))