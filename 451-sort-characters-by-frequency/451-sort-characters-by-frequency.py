class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0) + 1
            
        ans = sorted(d.items(),key = lambda x:[-x[1],x[0]])
        
        ans = [ch*n for ch,n in ans]
        
        return ''.join(ans)
        