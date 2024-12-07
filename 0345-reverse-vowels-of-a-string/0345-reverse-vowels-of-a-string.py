class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = ("a","e","i","o","u")
        vowels_list = []
        result = ""
        
        for ele in s:
            if ele.lower() in vowel_set:
                vowels_list.append(ele)
        
        for ele in s:
            if ele.lower() in vowel_set:
                result += vowels_list.pop()
            else:
                result += ele
                
        return result
        