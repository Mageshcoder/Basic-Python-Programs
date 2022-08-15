def mergeSort(mtlist):
   if len(mylist)>1:
      mid = len(mylist)//2
      left=mylist[:mid]
      right=mylist[mid:]
      mergeSort(left)
      mergeSort(right)
      i=j=k=0
      while i<len(left) and j<len(right):
         if left[i]<right[j]:
            mylist[k]=left[i]
            i+=1
         else:
            mylist[k]=right[j]
            j+=1
         k+=1

      while i<len(left):
         mylist[k]=left[i]
         i+=1
         k+=1
      while i<len(right):
         mylist[k]=right[j]
         j+=1
         k+=1
mylist=[54,6,93,100,77,31,44,55,12]
mergeSort(mylist)
print(mylist)
