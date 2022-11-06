class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        ans = 0
        i = 0

        for i,char in enumerate(s):
            if char in d:
                #update ans because we will change start
                ans = max(ans,i - start)
                
                #no need to go back behind start
                #if i is behind start,start remains same
                start = max(d[char] + 1,start)

            d[char] = i

        return max(ans,len(s) - start)
