class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(s = [],left = 0,right = 0):
            if len(s) == 2 * n:
                ans.append(''.join(s))
                return

            if left < n:
                s.append('(')
                generate(s,left + 1,right)
                s.pop()

            if right < left:
                s.append(')')
                generate(s,left,right + 1)
                s.pop()

        generate()
        return ans
