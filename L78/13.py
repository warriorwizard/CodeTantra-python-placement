a=input('Enter file name: ')
file=open(a,"rt")
data=file.read()
chr1=len(data)
words=data.split()
def counter(fname):
	num_words=0
	num_lines=0
	num_charc=0
	with open(a,'r') as f:
		for line in f:
			num_lines +=1
			word ='Y'
		# for letter in line:
		# 	if (letter != ' ' and word =='Y'):
		# 		num_words+=1
		# 		word='N'
		# for line1 in f:
		# 	words=line1.split()
		# 	num_words+=len(words)
		# data=
	print("Lines =",num_lines)
# print("words =",len(words))
	# print("Characters =",num_charc)
if __name__=='__main__':
	fname=a
	try:
		counter(fname)
	except:
		print('File not found')

print("words =",len(words))
print("Characters =",chr1)
					