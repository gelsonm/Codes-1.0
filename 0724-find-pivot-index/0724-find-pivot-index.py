class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        right_sum = 0
        left_sum = 0
        
        for num in nums:
            right_sum += num
            
        for i in range(len(nums)):
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
            
        return -1