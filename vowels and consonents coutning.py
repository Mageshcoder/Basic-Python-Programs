con_count=0
vow_count=0
str=input("enter your string to count Vowels and Consonents")
a=str.lower()

for i in range(0,len(a)):
	if (str[i] in ('a','e','i','o','u')):
		vow_count=vow_count+1

con_count=len(a)-vow_count
		
print("total no of vowels in a given string",vow_count)
print("total no of consonents in a given string",con_count)
