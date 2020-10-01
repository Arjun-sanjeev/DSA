def merge(arr,start,mid,end):
  result = [0]*(end-start+1)
  i = start
  j = mid+1
  k = 0

  while(i<=mid and j<=end):
    if(arr[i]>arr[j]):
      result[k] = arr[j]
      j+=1
      k+=1
    if(arr[i]<=arr[j]):
      result[k] = arr[i]
      i+=1
      k+=1
  while(i<=mid):
    result[k] = arr[i]
    k+=1
    i+=1
  while(j<=end):
    result[k] = arr[j]
    k+=1
    j+=1
  print(result)

def mergeSort(arr,start,end):
  if(start<end):
    mid = (start+end)//2
    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,start,mid,end)

mergeSort([4,2,5,1,7],0,4)