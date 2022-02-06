# First Solution saves memory but it's slow
digits = [1,2,3]
num = ""
for n in digits: 
    n = str(n)
    num += n
num = int(num) + 1

digits = [int(n) for n in str(num)]

print(num)
print(digits)

print([1] + [0] * len(digits))


# Second Solution

def plusOne(digits):
    # Find the first digit that's not 9, plus 1 and set all the numbers behind it to zero.
    index = -1

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            index = i
            digits[i] += 1
            break
        else:
            digits[i] = 0

    # Didn't find any 9's 
    if index == -1:
        return [1] + [0] * len(digits)

    return digits

# Third Solution

def plusOne_3(digits):
    rest = 1
    for idx in reversed(range(len(digits))):
        value = digits[idx] + rest
        if value > 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            rest = 0
            break
    if rest == 1:
        digits = [1] + digits
    return digits

print(plusOne_3([9, 9]))
