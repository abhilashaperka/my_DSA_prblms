#permutation difference (or distance) between two strings
class Solution:
    def findpermdiff(self, s:str, t:str) -> int:
        ind_s={char: index for index, char in enumerate(s)}
        ind_t={char: index for index, char in enumerate(t)}
        permutation_diff=0
        for char in s:
            permutation_diff+=abs(ind_s[char]-ind_t[char])    
        return permutation_diff
solution=Solution()
print(solution.findpermdiff("abc","bac"))
print(solution.findpermdiff("abcde","edbac"))
    

