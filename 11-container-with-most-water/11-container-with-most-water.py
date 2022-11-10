class Solution:
    def maxArea(self, height: List[int]) -> int:
        d = {}
        largest = 0
        i,j =0,len(height)-1

        left = height[i]
        right = height[j]
        
        while i<j:
            minimum = min(left,right)
            area = (j-i)*minimum
            
            if largest<area:
                largest = area
                
            if height[i]<height[j]:
                i = i + 1
                left = height[i]

            else:
                j = j - 1
                right = height[j]
            
        return largest  
    
    