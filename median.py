from typing import List
import math 

data = [64,6,92,7,70,5]
# [64,6,92,7,70,5]
# [64,6,92,7,70,5,9]

def median(data: List[int]): 
    data = sorted(data)
    length = len(data)%2
    if not length ==0:
        return data[math.floor(len(data)/2)]
    else:
    #elif length == 0: 
        return (data[len(data)//2] + data[(len(data)//2)-1]) / 2

print(median(data))
