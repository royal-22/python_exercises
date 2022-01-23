
def countInversion(sequence): 

    sequence, suma = list(sequence), 0

    while sequence != sorted(sequence): 
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[i+1]: 
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
                suma += 1
    return suma

if __name__ == "__main__": 
    print(countInversion([1, 2, 5, 3, 4, 7, 6]))
    print(countInversion([99, -99]))
    print(countInversion([5, 3, 2, 1, 0]))
