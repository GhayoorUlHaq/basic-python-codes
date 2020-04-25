def max_in_list(list, max):
    if len(list) == 0:
        return max
    else:
        temp_max = max
        if list[0] > max:
            temp_max = list[0]
        return max_in_list(list[1:], temp_max)

def find_max_wrapper(list):
    return max_in_list(list, 0)

print(find_max_wrapper([6,2,100,4,5]))