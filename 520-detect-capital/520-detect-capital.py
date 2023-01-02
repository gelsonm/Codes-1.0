class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        up_count = False
        low_count = False
        
        if word[0].isupper():
            word = word[1:]
            
        for letter in word:
            if letter.isupper():
                if low_count:
                    return False
                up_count = True
            else:
                if up_count:
                    return False
                low_count = True
                
        return True