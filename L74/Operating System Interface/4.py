import os
print('statistics:',os.stat('Some_File.txt'))
tup=os.walk(os.getcwd())
for dirpath, dirname, filename in tup:
	print("path:",dirpath)
	print("dir name:", dirname)
	print("file name:", filename)