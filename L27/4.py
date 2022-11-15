a=input('ch: ')
b='aeiouAEIOU'
if a.isalpha():
	if a in b:
		print('letter and vowel')
	else:
		print('letter and consonant')
else:
	print('not letter')