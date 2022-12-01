class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i in range(len(nums)):
#             val = target-nums[i]
#             if d.get(val) is not None:
#                 return [d[val],i]
#             else:
#                 d[nums[i]]=i
                
        d = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in d:
                return [d[val],i]
            else:
                d[nums[i]] = i