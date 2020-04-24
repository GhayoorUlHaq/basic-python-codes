def binary_search(list, number, start, end):
    if start > end:
        return None
    else:
        mid = (start+end)//2
        guess = list[mid]
        if guess == number:
            return mid
        elif guess > number:
            return binary_search(list, number, start, mid - 1)
        else:
            return binary_search(list, number, mid + 1, end)

def binary_search_wrapper(list, number):
    start = 0
    end = len(list) - 1
    return binary_search(list, number, start, end)

l1 = list(set(range(1421, 4213412)))
print(binary_search_wrapper(l1, 12341))
