#Program to remove punctuation marks from a string
import string
punctuations = string.punctuation
result = " "
str = "List - []\n tuple - ()\n Dictionary - {}\n Comment - #\n Multiply - *\n not - !\n and - &\n or - |\n format specifier - %\n String - " " $ @ ; : ' / + = "


#write your code here for removing punctuation
for i in str:
	if i not in punctuations:
		result = result + i



print("Set of punctuations in string.punctuation is:", punctuations) # print punctuations
	# else:
print("String after removing all Punctuation's is:", result) # print result here