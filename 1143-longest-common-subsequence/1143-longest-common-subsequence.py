class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        def helper(text1,text2,i,j,memo):
            
            #one or both of the strings are fully traversed
            if i == len(text1) or j == len(text2):
                return 0
            # if result of the pair is already in memo
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i] == text2[j]:
                #check for the next character in both strings
                memo[i][j] = helper(text1,text2,i+1,j+1,memo) + 1
            else:
                #check the maximum answer using the two options
                memo[i][j] = max(helper(text1,text2,i+1,j,memo),helper(text1,text2,i,j+1,memo))
            return memo[i][j]
        return helper(text1,text2,0,0,memo)