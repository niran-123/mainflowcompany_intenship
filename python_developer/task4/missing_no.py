def find_missing_number(arr):
    n = len(arr) + 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)
    return expected_sum - actual_sum  
arr = [1, 2, 4, 5, 6]  
print("Missing number:", find_missing_number(arr))
