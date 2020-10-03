def binarySearch(arr,target):
  start = 0
  end = len(arr)-1

  while(start<=end):
    mid = start + (stop-start)//2
    #mid = (start+end)//2 Thos may cause integer overflow if start and stop are huge integers

    if(arr[mid]==target):
      return mid
    elif(arr[mid]<target):
      start = mid+1
    else:
      end = mid-1
  
  return -1


arr = [1,3,5,7,9,16,42,39]
target = 142
print(binarySearch(arr,target))