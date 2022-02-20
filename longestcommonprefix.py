def longestCommonPrefix(strs: list) -> str:
        result = ""
        i = 0
        while i < len(min(strs)): 
            result += strs[0][i]
            for n in range(len(strs)): 
                for c in range(i+1):
                    if strs[n][c] == result: 
                        continue
                    else: 
                        if i == 0: 
                            return ""
                        else:
                            return result
            i+=1

ls = ["dog","racecar","car"]  #["flower","flow","flight"]
print(longestCommonPrefix(ls))

def longestCommonPrefix_2(strs: list) -> str: 
    result = ""
    for i in range(len(strs[0])):
        for s in strs: 
            if i == len(s) or [i] != strs[0][i]: 
                return result
        result += strs[0][i]
    return result


def longestCommonPrefi_3x(self, strs: list) -> str:
    shortest = strs[0]
    for str in strs:
        if len(str) < len(shortest):
            shortest = str
    
    prefix = ""
    for i in range(len(shortest)):
        for str in strs:
            if str[i] != shortest[i]:
                return prefix
        
        prefix += shortest[i]
    
    return prefix
