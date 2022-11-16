import os
try:
	print("file name:", os.ctermid())
	
	print("groups list:", os.getgroups() )# print the user group details using os.getgroups
except TypeError:
	print("exception on getting one of the details")