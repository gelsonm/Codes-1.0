# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def find(low,high):
            num = (low + high) // 2
            check = guess(num)
            
            if check == 0:
                return num
            elif check == 1:
                return find(num+1,high)
            else:
                return find(low,num-1)
            
        return find(1,n)