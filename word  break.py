#word break
def wordbreak(s, worddict):
    n=len(s)
    dp=[True]
    for i in range(1,n+1):
        dp.append(any(dp[j] and s[j:1] in worddict for j in range(i)))   #j=0
        print(dp)
    return dp[-1]
s="catsanddog"
worddict=["cats","and","dog","sand","cat"]
print(wordbreak(s,worddict))