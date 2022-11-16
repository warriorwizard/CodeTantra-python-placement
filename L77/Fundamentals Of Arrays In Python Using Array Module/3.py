import array as arr
value=arr.array('d',[1.2,2.3,3.4,5.5,7.6,10.8])
value[0]=0.5
print(value)
value[2:5]=arr.array('d',[4.9,6.9,8.9])
print(value)
# array('')