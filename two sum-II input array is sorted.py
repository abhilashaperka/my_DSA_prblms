def twosumII(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum > target:
            right = right - 1
        elif sum < target:
            left = left + 1
        else:
            return [left + 1, right + 1]
    return [-1, -1]
a=[1,2,4,6,8,9,34,68,89]
t=17
print(twosumII(a,t))
