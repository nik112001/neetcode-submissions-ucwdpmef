class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        initialPrice = prices[0]
        for num in prices[1:]:
            if num < initialPrice:
                initialPrice = num
            else:
                maxProfit = max(maxProfit,num - initialPrice)
        return maxProfit