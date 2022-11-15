def r_sum(nested_num_list):
	total=0
	for j in range(len(nested_num_list)):
		if type(nested_num_list[j])==list:
			total +=r_sum(nested_num_list[j])
			
		else:
			total+=nested_num_list[j]
	return total
			
# write your code here


	
L1 = [1, 10, 9, [3, 5, 7], [5, [6, 7], 97]]
print(r_sum(L1))