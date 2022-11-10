class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        
        for ele in s:
            d[ele] = d.get(ele,0) + 1
            
        for ele in t:
            d[ele] = d.get(ele,0) - 1
            
            if d[ele] < 0:
                return ele
       
        