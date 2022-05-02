from matplotlib import collections


def groupAnagrams(strs):
    
    if strs == [""]:
        return [[""]]
    if len(strs) == 1: 
        return [[strs[0]]]
    
    res = []
    
    for w in strs: 
                    
        if len(res) > 0:
            for i in range(len(res)):
                if sorted(w) == sorted(res[i][0]):
                    print(w)
                    res[i].append(w)
                    break
            else:
                res.append([w])
                print(res)
                
        if len(res) == 0: 
            res.append([w])
        

    return res
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

def groupAnagrams_2(strs):
    res = collections.defaultdict(list)
    for w in strs:
        res[tuple(sorted(w))].append(w)
    return res.values()

def groupAnagrams(strs):
    
    anagrams = {}

    for s in strs: 

        s_sort = "".join(sorted(list(s)))

        if s_sort not in anagrams: 
            anagrams[s_sort] = []
        anagrams[s_sort].append(s)

    return list(anagrams.values())

