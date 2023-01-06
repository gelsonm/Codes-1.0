class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            return nums.reverse()
        
        n = len(nums) - 2
        
        while n>=0 and nums[n] >= nums[n+1]:
            n = n-1
            
        if n == -1:
            return nums.reverse()
        
        for i in range(len(nums)-1,n,-1):
            if nums[i] > nums[n]:
                nums[n],nums[i] = nums[i], nums[n]
                break
                
        # return nums[:n+1] + nums[n+1:].reverse()
        nums[n+1:] = reversed(nums[n+1:])  
        return nums
        