li='aeiouAEIOU'
while True:
	a=str(input('vowel, or 9 to quit: '))
	if a.isalpha():
		if a in li:
			print('vowel')
		else:
			print('not vowel')
	elif a.isalnum():
			if a=='9':
				break
			else:
				print('wrong input')
	else:
			print('wrong input')