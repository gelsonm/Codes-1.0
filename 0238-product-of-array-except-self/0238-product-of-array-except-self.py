class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_product = 1
        length = len(nums)
        ans = [1] * length

        for i in range(length):
            ans[i] = ans[i] * curr_product
            curr_product = curr_product * nums[i]
            # print(i,"->",ans[i],end="|")
        
        # print("---")
        curr_product = 1
        for i in range(length-1,-1,-1):
            ans[i] = ans[i] * curr_product
            curr_product = curr_product * nums[i]
            # print(i,"->",ans[i],end="|")
        return ans
            