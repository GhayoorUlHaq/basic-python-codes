def count_list(list, count):
    if len(list) == 0:
        return count
    else:
        return 1 + count_list(list[1:], count)

def count_list_wrapper(list):
    return count_list(list, 0)

print(count_list_wrapper([1,2,3,4,5]))