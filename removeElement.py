nums = [3,2,2,3] #[0,1,2,2,3,0,4,2]
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

print(nums)

# Second solution

def removeElement(nums:list, val: int)->list: 
    n = 0
    while n < len(nums):
        if(nums[n] == val):
            for i in range(-(len(nums)-1), n):
                abs(i)
                temp = nums[i]
                nums[i-1] = temp
                nums[i] = nums[i-1]
        n+=1
    return nums

print(removeElement(nums, val))

# Third Solution

nums.sort(key=lambda x: x!=val, reverse=True)
n = 0
while True:
    if nums[n] == val: 
        break
    n+=1
print(nums[:n])
print(n)
