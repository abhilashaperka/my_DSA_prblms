def length_of_longest_substrng(s):
    n=len(s)
    maxlen=0
    charset=set()
    left=0
    for right in range(n):
        if s[right] not in charset:
            charset.add(s[right])
            maxlen=max(maxlen,right-left+1)
        else:
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
    return maxlen
a="awwkgde"
print(length_of_longest_substrng(a))