st2cap = dict()
state = input("state or 'end' to quit: ")
if state == 'end':
	pass
else:
	

    capital=input("capital: ")
    st2cap[state]=capital
while state != 'end':
	state=input('state: ')
	if state=='end':
		break
	else:
		
		capital=input('capital: ')
		st2cap[state]=capital
	




# write your logic using while loop

# take inputs capital anad state from the user and store it in a dictionary till the user enters state as end

print(sorted(st2cap.items()))