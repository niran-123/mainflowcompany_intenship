def second_largest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return "No second largest element"
    unique_lst.sort(reverse=True)
    return unique_lst[1]  
nums = [10, 20, 4, 45, 99, 99]
print(second_largest(nums))
