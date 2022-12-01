class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        count = 0
        
        for i in range(mid):
            if s[i] in vowels:
                count += 1
                
            if s[mid+i] in vowels:
                count -= 1
        
        return count == 0