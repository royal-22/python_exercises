import re
def palidrome(s:str)->bool:
    s = s.lower()
    """s = s.lower()
    for n in s: 
        pali.append(ord(n))
    print(pali)
    return 0"""

    pali = [x for x in s if (ord(x) >= 97 and ord(x) <= 122) or (ord(x) >= 48 and ord(x) <= 57)]
    return "".join(pali) == "".join(pali)[::-1]

wr = "0P" #"race a car" #"A man, a plan, a canal: Panama"


print(palidrome(wr))

def palidrome_2(s:str)->bool: 
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    if s == s[::-1]:
        return True
    return False

def palidrome_3(s:str)->bool: 
    s = s.lower()
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True
