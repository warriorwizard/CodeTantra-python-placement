s=list(input('str: '))
stack=[]
key=True
count=0
ran=0
for i in range(len(s)):
	if s[i]=='(':
		count+=1
		stack.append('(')
	elif s[i]==')':
		if len(stack)==0:
			key=False
			ran+=1
		else:
			stack.pop()
if len(stack)!=0:
	key=False
	ran=len(stack)
if key==False:
	print('not valid and errors:',ran)
else:
	print('valid and depth:',count)
	