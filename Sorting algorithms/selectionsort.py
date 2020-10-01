def minindexselection(arr,i,end):
  min_index = i
  i += 1
  while(i<end):
    if(arr[i]<arr[min_index]):
      min_index = i
    i += 1
  return min_index    
      

def selectionSort(arr,end):
  i = 0

  while(i<end):
    index = minindexselection(arr,i,end)

    if(index != i):
      arr[i],arr[index] = arr[index],arr[i]

    i += 1 


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
selectionSort(arr,n) 
print ("Sorted array is:") 
for i in range(n): 
	print (arr[i])
	