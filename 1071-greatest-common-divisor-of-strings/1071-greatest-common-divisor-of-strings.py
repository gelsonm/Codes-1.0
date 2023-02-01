class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # len1 = min(len(str1), len(str2))
        # for i in range(len1, 0, -1):
        #     if len(str1) % i == 0 and len(str2) % i == 0:
        #         sub1 = str1[:i]
        #         sub2 = str2[:i]
        #         if sub1 * (len(str1) // i) == str1 and sub1 * (len(str2) // i) == str2:
        #             return sub1
        # return ""

        len1 = min(len(str1),len(str2))
        for i in range(len1,0,-1):
            if len(str1) % i ==0 and len(str2) % i ==0:
                sub1 = str1[:i]
                sub2 = str2[:i]
                
                if sub1 * (len(str1) // i) == str1 and sub1 * (len(str2) // i) == str2:
                    return sub1
                
        return ""