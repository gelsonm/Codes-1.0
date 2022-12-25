class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        A = nums
        Q = queries
        A.sort()
        A = list(accumulate(A))
        return [bisect_right(A, q) for q in Q] 