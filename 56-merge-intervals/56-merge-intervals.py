class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda v:(v[0],v[1]))
        
        ans = [intervals[0]]
        
        for s,e in intervals:
            end = ans[-1][1]
            if s<=end:
                ans[-1][1] = max(end,e)
            else:
                ans.append([s,e])
                
        return ans
                
            
                
            
            