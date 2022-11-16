
a,b,c=map(int,input("Enter x, y, r of ball-1: ").split())
d,e,f=map(int,input("Enter x, y, r of ball-2: ").split())
dis=c+f
cal=((a-d)**2+(b-e)**2)**0.5
if dis<cal:
	print('False - Balls are not colliding')
else:
	print('True - Balls are colliding')
	