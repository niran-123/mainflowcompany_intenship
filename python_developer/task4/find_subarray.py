def find_subarray_with_sum(arr, S):
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > S and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == S:
            return (left, right)

    return -1  
arr = [1, 2, 3, 7, 5]
S = 12
print("Subarray indices:", find_subarray_with_sum(arr, S))  
