class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        ans = 0
        
        for sell in range(1,len(prices)):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                ans = max(ans,profit) 
            else:
                profit = 0
                buy = sell
                
        return ans