b=[]
def solution(a,n,subset,s):
    global ctr
    ctr=0
    if(s==0):
        a.append(subset)
        return
    if(n==0):
        return
    if(a[n-1]<=s):
        solution(a,n-1,subset,s)
        solution(a,n-1,subset+str(a[n-1])+"",s-a[n-1])
    else:
        solution(a,n-1,subset,s)
print("enter list of integers:",end=" ")
a=[int(x) for x in input().split()]
s=int (input("enter the sum value:"))
subset=" "
solution(a,len(a),subset,s)
for i in b:
    print("solution",ctr,"--->",i)
    ctr=ctr+1
print("the total number of solution for sum of subsets is:",len(b))
