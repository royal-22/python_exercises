def canMakeArithmeticProgression(arr:list) -> bool:
    arr.sort()
    progression = arr[1] - arr[0]
    print(progression)
    for i in range(1, len(arr)-1):
        current = arr[i+1] - arr[i]
        print(current)
        if current != progression:
            return False
    return True

print(canMakeArithmeticProgression(
[-68,-96,-12,-40,16]))
