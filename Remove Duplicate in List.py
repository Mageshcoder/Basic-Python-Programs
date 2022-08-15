
#test_list = [1, 3, 5, 6, 3, 5, 6, 1,4,45,5,6,3,345,6,6,7,85,4,22,4,4,7,4,7,5,3,5,7,9,9,8,6,23,234,4,7,56,764]
#print ("The original list is : " + str(test_list))

old_array=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
new_array = []
for i in old_array:
	if i not in new_array:
		new_array.append(i)
print(str(new_array))

#print ("The list after removing duplicates : " + str(res))
