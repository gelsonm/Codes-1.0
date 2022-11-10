class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack) - len(needle) + 1):
            k = 0
            for j in range(len(needle)):
                if haystack[i] == needle[j]:
                    i += 1
                    k += 1
                else:
                    break
                    
            if k == len(needle):
                return i - k
            
        return -1