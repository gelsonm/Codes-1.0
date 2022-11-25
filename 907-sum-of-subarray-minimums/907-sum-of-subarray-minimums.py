class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res, stack = 0, [-1]
        for i in range(len(arr)+1):
            while stack[-1]!=-1 and (i==len(arr) or arr[i] <= arr[stack[-1]]):
                idx, l, r = stack.pop(), stack[-1], i
                res = (res + (r-idx) * (idx-l) * arr[idx]) % 1000000007
            stack.append(i)
        return res
        