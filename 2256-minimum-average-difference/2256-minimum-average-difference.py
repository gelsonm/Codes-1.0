import numpy as np

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        first, last = [], [0]
        f = l = 0
        
        for i,n in enumerate(nums,start=1):
            first.append((f:=f+n) // i)

        for i,n in enumerate(reversed(nums[1:]),start=1):
            last.append((l:=l+n) // i)
            
        last.reverse()
        
        diff = [abs(f-l) for f,l in zip(first,last)]
        
        return np.argmin(diff)