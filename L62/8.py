fin = open('InputData3.txt', 'r')			#Open the text Files for input and output
fout = open('OutputData3.txt', 'w')			#if the file is big we will read and write line by line.
for i in fin:
	# i=i.rstrip()
	fout.write(i)
	
	print(i.rstrip('\n'))
	
    				        #Write the line
fin.close()					#Close the input file
fout.close()                #Close the output file
			                #Close the input file
               				#Close the output file
fin = open('OutputData3.txt' , 'r')			#Open the new file as input
# for i in fin:
# 	i=i.rstrip()
# 	print(i)#for each line
    	     				#Print line
fin.close()               	#Close the File