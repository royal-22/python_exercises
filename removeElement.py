"""nums = [3,2,2,3] #[0,1,2,2,3,0,4,2]
val = 3

for n in range(len(nums)): 
    if nums[n] == val: 
        nums[n] = "_"

nums.sort(key=lambda x:type(x)==int, reverse=True)
n=0
while n < len(nums): 
    if nums[n] == "_":
        nums.pop(n)
        n-=1
    n+=1

print(nums)"""

# Second Solution

nums = [3,2,2,3]
val = 3

def removeElement(nums:list, val: int)->list: 
    k = 0
    for i in range(len(nums)): 
        if (nums[i] != val): 
            nums[k] = nums[i]
            k += 1
    print(nums[:k])
    return k

print(removeElement([3, 2, 2, 3], val))

# Third Solution

"""nums.sort(key=lambda x: x!=val, reverse=True)
print(nums)
n = 0
while True:
    if nums[n] == val: 
        break
    n+=1
print(nums[:n])
print(n)"""
