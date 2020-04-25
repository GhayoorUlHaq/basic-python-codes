def sum_list(list):
    if len(list) <= 0:
        return 0
    else:
        return list[0] + sum_list(list[1:])

print(sum_list([1,2,3,4,5]))