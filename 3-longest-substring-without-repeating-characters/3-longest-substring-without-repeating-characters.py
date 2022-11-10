class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        start = 0
        ans = 0
        i = 0

        for i,char in enumerate(s):
            if char in d:
                ans = max(ans,i - start)

                start = max(start,d[char] + 1)

            d[char] = i

        ans = max(ans,len(s) - start)

        return ans

