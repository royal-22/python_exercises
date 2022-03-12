def replaceElement(arr:list)->list: 
    i = 0
    length = len(arr)
    while i < length: 
        if i < length -1:
            arr[i] = max(arr[i+1:])
        else:
            arr[i] = -1
        i+=1
    return arr

print(replaceElement([17,18,5,4,6,1]))
