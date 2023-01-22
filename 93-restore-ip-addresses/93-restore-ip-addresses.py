class Solution:
    def valid(self, s: str, start: int, length: int) -> bool:
        return length == 1 or (s[start] != '0' and (length < 3 or s[start:start+length] <= "255"))

    def helper(self, s: str, startIndex: int, dots: List[int], ans: List[str]) -> None:
        remainingLength = len(s) - startIndex
        remainingNumberOfIntegers = 4 - len(dots)

        if remainingLength > remainingNumberOfIntegers * 3 or remainingLength < remainingNumberOfIntegers:
            return
        if len(dots) == 3:
            if self.valid(s, startIndex, remainingLength):
                temp = ""
                last = 0
                for dot in dots:
                    temp += s[last:last+dot]
                    last += dot
                    temp += "."
                temp += s[startIndex:]
                ans.append(temp)
            return
        for curPos in range(1, min(4, remainingLength+1)):
            dots.append(curPos)
            if self.valid(s, startIndex, curPos):
                self.helper(s, startIndex + curPos, dots, ans)
            dots.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        dots = []
        ans = []
        self.helper(s, 0, dots, ans)
        return ans