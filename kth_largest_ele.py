def find_kth_largest(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Return the kth largest element
    return arr[k-1] if k <= len(arr) else None

# Take user input for the array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Take user input for the value of k
k = int(input("Enter the value of k for kth largest element: "))

result = find_kth_largest(arr, k)

if result is not None:
    print(f"The {k}th largest element in the array is:", result)
else:
    print("Invalid input. Check the value of k.")
