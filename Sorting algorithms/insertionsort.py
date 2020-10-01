def insertionSort(arr):
  length = len(arr)

  for i in range(length):
    temp = arr[i]
    j=i-1
    while(j >= 0):
      if(arr[j]>temp):
        arr[j+1] = arr[j]
        arr[j] = temp
        j -= 1
      elif(arr[j]<=temp):
        break
  print(arr)


insertionSort([9,4,5,2,7,6,1,2])