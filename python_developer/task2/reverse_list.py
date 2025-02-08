def reverse_list(lst):
    return lst[::-1] 
nums = list(map(int, input("Enter no's separated by spaces: ").split()))
print("Reversed List:", reverse_list(nums))
