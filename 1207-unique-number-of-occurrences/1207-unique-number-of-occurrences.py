class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # I MISS YOU
        return len(set(arr)) == len(set(Counter(arr).values()))
        