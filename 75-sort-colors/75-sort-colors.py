class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Brute Force
        # Initialize counters for 0s, 1s, and 2s
        zero_count = one_count = two_count = 0
        # Count the number of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
        # Overwrite the array with the sorted values
        for i in range(zero_count):
            nums[i] = 0
        for i in range(zero_count, zero_count + one_count):
            nums[i] = 1
        for i in range(zero_count + one_count, len(nums)):
            nums[i] = 2
            
            
        # Dutch National Flag algorithm
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1
                
                
        