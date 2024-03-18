from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remove duplicates using set and convert back to list
        l = list(set(nums))
        # Sort the list in ascending order
        l.sort()
        # Check if the list has at least 3 elements
        if len(l) >= 3:
            # Return the third maximum element
            return l[len(l)-3]
        # If there are fewer than 3 elements, return the maximum element
        return max(l)

if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Take user input for the list of numbers
    input_nums = input("Enter the list of numbers separated by spaces: ")
    nums_list = list(map(int, input_nums.split()))

    # Call the thirdMax method with user-provided input
    result = sol.thirdMax(nums_list)

    if result is not None:
        print(f"The third maximum element in the array is: {result}")
    else:
        print("Invalid input. Check the list of numbers.")
