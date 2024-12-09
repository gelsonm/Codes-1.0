class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        max_reach = [0] * n
        end = 0

        for start in range(n):
            end = max(end, start)

            while end < n - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
                
            max_reach[start] = end

        ans = []

        for start, end_query in queries:
            ans.append(end_query <= max_reach[start])
    
        return ans
    