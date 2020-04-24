def binary_search(list, number):
    start = 0
    end = len(list)-1
    while(start <= end):
        mid = (start+end)//2
        guess = list[mid]
        if guess == number:
            return mid
        elif guess > number:
            end = mid - 1
        else:
            start = mid+1
    return None


l1 = list(set(range(1421, 4213412)))
print(binary_search(l1, 12341))