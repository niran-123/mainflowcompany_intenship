def sort_list_builtin(lst):
    return sorted(lst) 
nums = list(map(int, input("Enter no's separated by spaces: ").split()))
print("Sorted List:", sort_list_builtin(nums))
