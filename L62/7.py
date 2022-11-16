fin = open('InputData2.txt' , 'r')
charCount = wordCount = lineCount = 0			#Initialize Counters
for line in fin:								#Read each Line
	lineCount+=1
	# write your logic here
	temp=len(str(line).split())
	wordCount+=temp
	#Increment Line count
	for i in line:
		if i!=" " or i!='\n':
			charCount+=1

	#split() gives the words in a list

	#Increment Character Count

print("Line count = ", lineCount)  #Print the Counts
print("Word count = ", wordCount)
print("Char count = ", charCount)