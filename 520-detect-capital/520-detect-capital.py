class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        up_count = False
        low_count = False
        
        for i,l in enumerate(word):
            if l.isupper():
                if low_count:
                    return False
                if i != 0:
                    up_count = True
                    
            else:
                if up_count:
                    return False
                
                low_count = True
                
        return True