def countpairs(nums,target):
    nums.sort()
    left=0
    right=len(nums)-1
    while(left<right):
        if(nums[left]+nums[right]<target):
            count+=right-left
            left+=1
        else:
            right+=1
    return count
n=[-6,2,5,-2,-7,1,3]
t=-3
r=countpairs(n,t)
print(r)