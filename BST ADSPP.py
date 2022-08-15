def BS(arr,low,high,x):
    if high>=low:
        mid = (high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return BS(arr,low,mid-1,x)
        else:
            return BS(arr,mid+1,high,x)
    else:
        return -1

arr = [2,3,4,10,40]
x=10
result = BS(arr,0,len(arr)-1,x)
if result!=-1:
    print("ELEMENT IS PRESENT AT INDEX  ",str(result),"OF AN ARRAY")
else:
    print("ELEMENT IS NOT PRESENT IN AN ARRAY")
