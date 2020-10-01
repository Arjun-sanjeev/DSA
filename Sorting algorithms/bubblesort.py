def bubbleSort(arr,length):
  for i in range(length):
    for j in range(length):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1] = arr[j+1],arr[j]
  print(arr)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
bubbleSort(arr,n-1) 