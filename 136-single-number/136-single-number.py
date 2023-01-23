class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute force
        "'''"
#         freq = {}
        
#         for num in nums:
#             freq[num] = freq.get(num,0) + 1
            
#         for num in freq:
#             if freq[num] == 1:
#                 return num
        "'''"
    
        # XOR bits
        ans = nums[0]
        
        for num in nums[1:]:
            ans ^= num
            
        return ans