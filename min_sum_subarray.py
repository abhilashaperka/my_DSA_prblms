def min_sum_subarray(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []

    min_sum = float('inf')
    current_sum = sum(arr[:k])
    min_start = current_sum = sum(arr[:k])
    for i in range(len(arr) - k + 1):
        if current_sum < min_sum:
            min_sum = current_sum
            min_start = i

        if i + k < len(arr):
            current_sum = current_sum - arr[i] + arr[i + k]
    return min_sum


    
# Take user input for the list of numbers
input_str = input("Enter a list of numbers separated by spaces: ")
arr = [int(num) for num in input_str.split()]

# Take user input for the size of subarray (k)
k = int(input("Enter the size of subarray (k): "))

result = min_sum_subarray(arr, k)
if result:
    print(f"Minimum sum subarray of size {k}: {result}")
else:
    print("No subarray found.")
