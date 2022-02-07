def thirdMax(nums:list)->int: 
    nums.sort(reverse=True)
    print(nums)
    n = 0
    nf = 0
    i = 0
    if len(nums) < 3: 
            return max(nums)

    
    while nf < 2 and i < len(nums)-1:
        if nums[i] != nums[i+1]:
            n+=1
            nf +=1
               
                #print(numsfound)
        elif nums[i] == nums[i+1]:                
            n+=1
        i+=1
    
    if nf==1 and i==len(nums)-1:
        return max(nums)

    #print(nf)
    return nums[n]




def thirdMax2(nums:list)->int: 
    res = []
    while nums:
        max_num = max(nums)
        res.append(max_num)
        nums = list(filter(lambda x: x != max_num ,nums))
        
        
    print(res)
        
        
       
    if len(res) >= 3:
        return res[2]
    else:
        return max(res)
            
print(thirdMax2([2,2,3,1]))
