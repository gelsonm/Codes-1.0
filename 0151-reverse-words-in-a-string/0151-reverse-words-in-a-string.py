class Solution:
    def reverseWords(self, s: str) -> str:
        s_splitted = s.split(" ")
        result = ""
        
        for ele in s_splitted:
            if ele:
                result = ele + " " + result           
            
        return result.strip()