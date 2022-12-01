class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPalindrome(s,i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        ans = ''
        for i in range(len(s)):
            ans = max(checkPalindrome(s,i,i),checkPalindrome(s,i,i+1),ans,key=len)
            
        return ans