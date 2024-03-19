def isSubsetSum(a, n, s) :
	if (s == 0) :
		return True
	if (n == 0 and s != 0) :
		return False	
	if (a[n - 1] > s) :
		return isSubsetSum(a, n - 1, s);
	return isSubsetSum(a, n-1, s) or isSubsetSum(a, n-1, s-s[n-1])
a = [3, 34, 4, 12, 5, 2]
s = 9
n = len(a)
if (isSubsetSum(a, n, s) == True) :
	print("Found a subset with given sum")
else :
	print("No subset with given sum")
