#isomorphic strings
def isIsomorphic(s,t):
    dic={}
    if(len(s)!=len(t)):
        return False
    if(len(set(s))!=len(set(t))):
        return False
    
    for i in range(len(s)):
        if(s[i] not in dic):
            dic[s[i]]=t[i]
        elif(dic[s[i]]!=dic[t[i]]):
            return False
        return True
s="abc"
t="def"
print(isIsomorphic(s,t))
