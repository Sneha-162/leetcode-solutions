class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = float('inf')
        maxProfit = 0 
        for i in range (0,n):
            minPrice = min(minPrice,prices[i])
            maxProfit = max(maxProfit,prices[i]-minPrice)
        return maxProfit
