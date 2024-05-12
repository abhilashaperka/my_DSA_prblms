def twosum(nums, target):
    store = {}
    for i, ele in enumerate(nums):
        if target - ele in store:
            return [store[target - ele], i]
        else:
            store[ele] = i

a = [7, 7, 4, 5, 3, 5, 1]
t = 9
print(twosum(a, t))
