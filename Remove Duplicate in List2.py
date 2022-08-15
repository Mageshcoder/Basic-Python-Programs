old_array=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
new_array = []
for i in old_array:
	if i not in new_array:
		new_array.append(i)
print(str(new_array))
