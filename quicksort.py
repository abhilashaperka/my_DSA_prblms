def partition(a, s, e):
    pi=a[e]
    i=s-1
    for j in range(s, e):
        if(a[j]<=pi):
            i=i+1
            a[i], a[j]= a[j], a[i]
    a[i+1], a[e]=a[e], a[i+1]
    return i+1
def quicksort(a, s, e):
    if s<e:
        p=partition(a, s, e)
        quicksort(a, s, p-1)
        quicksort(a, p+1, e)
#driver code
a=input('enter elements:').split()
a=[int(x) for x in a]
print('unsorted data',a)
quicksort(a, 0, len(a)-1)
print('sorted elements:')
print(a)
