def bubble(arr):
    lenght=len(arr)
    for j in range(0, lenght-1):
           if not isinstance(arr[j],(int,float)):
                return None
    
    for i in range(lenght):
        for j in range(0, lenght-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr