def maxwater(height):
    ans,i,j=0,0,len(height)-1
    while(i<j):
        if height[i]<=height[j]:
            res=height[i]*(j-1)
            i+=1
        else:
            res=height[j]*(j-i)
            j-=1
        if res>ans:ans=res
    return ans
h=[1,8,6,2,5,4,8,3,7]
r=maxwater(h)
print(r)