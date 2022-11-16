TryAgain=True
while TryAgain:
	try:
		Value=int(input("whole number: "))
	except ValueError:
		print("you must enter a whole number!")
		try:
			Again=input("try again (y/n)? ")
		except:
			print('OK, see you next time!')
			TryAgain=False
		else:
			if str.upper(Again)=='N':
				TryAgain=False
	except KeyborardInterrupt:
		print('you pressed Ctrl+c!')
		print("see you next time!")
	else:
		print(Value)
		TryAgain = True
		