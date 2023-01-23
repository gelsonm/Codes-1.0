class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n+1)
        
        if n == 1:
            return 1
        
        for a,b in trust:
            trusted[a] -= 1
            trusted[b] += 1
            
        for label in range(n+1):
            if trusted[label] == n - 1:
                return label
            
        return -1
        