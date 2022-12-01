class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        points = stones
        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})
        