class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
        i=0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == val:
                while (nums[j] == val and j>i):
                    j=j-1
                nums[i]=nums[j]
                counter += 1
                i+=1
                j=j-1
        counter = len(nums) - counter
        return counter
                
        