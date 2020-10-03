def spiralMatrix(A):

        
    top = 0
    bottom = ((A-1)*2)
    left = 0
    right = ((A-1)*2)


    w, h = right+1, right+1;
    arr = [[0 for x in range(w)] for y in range(h)]
        
    direction = 0
        
    num = A
    
    while(top<=bottom and left<=right):
        if direction == 0:
            for i in range(left,right+1):
                arr[top][i] = num
            direction = 1
            top += 1

        elif direction == 1:
            for i in range(top,bottom+1):

                arr[i][right] = num
            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right,left-1,-1):
                arr[bottom][i] = num
            direction = 3
            bottom -= 1

        elif direction == 3:
            for i in range(bottom,top-1,-1):
                arr[i][left] = num

            num -= 1
            left += 1
            direction = 0
        
    print(arr)


prettyPrint(3)