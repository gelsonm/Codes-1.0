class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total_product = 1
        result = []
        count_of_zeros = 0            
        
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                count_of_zeros += 1
                
        for num in nums:
            if num == 0:
                if count_of_zeros == 1:
                    result.append(total_product)
                else:
                    result.append(0)
            elif count_of_zeros > 0:      
                result.append(0)
            else:
                result.append(total_product//num)

        return result