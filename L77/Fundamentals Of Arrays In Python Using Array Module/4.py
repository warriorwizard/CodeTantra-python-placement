# Type your code here
import array as arr
values=arr.array('d',[1.2,2.3,3.4,5.5,7.6,10.8])
print("Size of array values is: ",len(values))
print(values)
del values[2]
print(values)
del values[2:4]
print(values)
