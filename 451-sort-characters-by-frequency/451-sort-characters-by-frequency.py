class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = defaultdict(lambda:0)
        
        for ch in s:
            d[ch] += 1
            
        res = sorted(d.items(),key = lambda item:[-item[1],item[0]])
        res = [ch*n for ch,n in res]
        # return ''.join(res.keys())
        return ''.join(res)
            
        