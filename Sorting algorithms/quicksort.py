def pivot(arr,start,end):

  i = start-1
  pivot = arr[end]

  for j in range(start,end):
    if(arr[j]<=pivot):
      i+=1
      arr[j],arr[i] = arr[i],arr[j]
      
    arr[end],arr[i+1] = arr[i+1],arr[end]  
  return i+1


def quickSort(arr,start,end):
  if(start<=end):
    pivot_index = pivot(arr,start,end)

    quickSort(arr,start,pivot_index-1)
    quickSort(arr,pivot_index+1,end)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print (arr[i])
	