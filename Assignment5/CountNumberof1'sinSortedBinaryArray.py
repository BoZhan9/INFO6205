def countOnes(arr, start, end):
     
    if end > start:
         
        mid = (start + end) // 2  
               
        if ((mid == high or arr[mid + 1] == 0) and arr[mid] == 1:
            return mid + 1             
        if arr[mid] == 1:
            return countOnes(arr, mid + 1, end)
             
        return countOnes(arr, start, mid - 1)
     
    return 0
 
                    