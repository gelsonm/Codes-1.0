class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted(intervals, key = lambda v:(v[0],v[1]))
        
        intervals.sort()
        ans = [intervals[0]]
        
        for s,e in intervals:
            if ans[-1][1] >= s:
                ans[-1][1] = max(e,ans[-1][1])
            else:
                ans.append([s,e])
                
        return ans
            
                
            
                
            
            