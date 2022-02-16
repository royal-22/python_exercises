# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:

    if needle == "": return 0
    if needle in haystack:
        i = haystack.index(needle)        
        return i
    else: 
        return -1

haystack = ""  #"hello"
needle = "" #"ll"

print(strStr(haystack, needle))


def strStr_2(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
        
    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:
            return i 
    return -1 
