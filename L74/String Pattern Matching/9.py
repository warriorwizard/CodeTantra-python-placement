# impirt re
import re

mystring = "The alternate email address is victory@ct.com"
match = re.search('(\w+)@(\w+).(\w+)', mystring)
if match:
	# find full match text and print the result
	print("Full match:",match.group())
	
	# find the match text corresponding to the 1st left parenthesis and print
	print("Group 1:",match.group(1))
	
	# find the match text corresponding to the 2nd left parenthesis and print
	print("Group 2:",match.group(2))
	
	# find the match text corresponding to the 3rd left parenthesis and print
	print("Group 3:",match.group(3))