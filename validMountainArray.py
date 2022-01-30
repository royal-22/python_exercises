def validMountainArray(arr:list)->bool: 
    N = len(arr)
    i = 0
    while i +1 < N and arr[i] < arr[i+1]: 
        i+=1
    
    if i == 0 or i == N - 1: 
        return False
    
    while i+1 < N and arr[i] > arr[i+1]:
        i+=1
    
    return i == N-1

print(validMountainArray([0, 3, 2, 1]))

def validMountainArray2(arr:list)->bool: 
    fh = 0
    sh = 0
    hi = arr.index(max(arr))
        
    for i in range(hi):
        if arr[i + 1] > arr[i]:
            fh = 1
        else:
            fh = 0
            break
        
    for i in range(hi, len(arr) - 1):
            
        if arr[i + 1] < arr[i]:
            sh = 1
        else:
            sh = 0
            break

    if fh == 1 and sh == 1:
        return True
    else:
        return False    


print(validMountainArray2([0, 3, 2, 1]))

# Alternative
"""        left, right = 0, len(arr)-1
        
        while left < len(arr)-2 and arr[left]<arr[left+1]:
            left+=1
        while right > 1 and arr[right]<arr[right-1]:
            right-=1
        
        return left == right if len(arr) >= 3 else False
"""

def validMountainArray3(arr:list) -> bool:
    if len(arr) < 3:
        return False
        
    maxarr = arr.index(max(arr))
        
    if maxarr == 0 or maxarr == len(arr) - 1: 
        return False
        
        
    left, right = arr[:maxarr], arr[maxarr:]
    s_left, s_right = sorted(left), sorted(right, reverse = True)
        
    return left == s_left and right == s_right and len(left) == len(set(left)) and len(right) == len(set(right)) 
