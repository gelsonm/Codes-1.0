class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        ans.append([1])
        
        for row in range(1,numRows):
            temp = [1]
            for i in range(1,row):
                val = ans[-1][i] + ans[-1][i-1]
                temp.append(val)
            temp.append(1)
            
            ans.append(temp)
            
        return ans
                