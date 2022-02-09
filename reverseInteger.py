def reverse(x):
    x = str(x)
    ls = [n for n in x if n != "0"]
    if ls[0] == "-": 
        ls[1:].reverse()    
    else:
        ls.reverse()

    num = "".join(ls)
    num = int(num)
    return num

print(reverse(x))

def reverse2(x): 
    if x<0:
        sign = -1
    else:
        sign = 1
        
    x = x * sign
    
    digits = list(str(x))
    reversednum = 0 
    exponent = 0
    for digit in digits:
        digit = int(digit)
        s =  (digit * 10**exponent)
        if reversednum+s>(2**31):
            return 0 
        reversednum = reversednum + s
        
        exponent = exponent + 1
        
    return reversednum*sign

def reverse3(x): 
    x = str(x)
    negative = False
    
    if x[0] == '-':
        negative = True
        x = x[1:]
    
    x = x[::-1]
    
    index = 0
    while x[index] == 0:
        index += 1
    
    result = int(x[index:])
    
    
    if negative:
        result = -1 * result
        
    if result > 2 ** 31 -1 or result < -2 ** 31:
        return 0
    
    else:
        return result
