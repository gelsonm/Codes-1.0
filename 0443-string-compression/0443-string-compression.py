class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        
        if len(chars) == 1:
            return 1
        
        while i < len(chars): 
            current_char = chars[i]
            current_count = 0
            
            while i < len(chars) and current_char == chars[i]:
                i += 1
                current_count += 1
            
            chars[k] = current_char
            k += 1
            
            if current_count > 1:
                for digit in str(current_count):
                    chars[k] = digit
                    k += 1
                
        return k