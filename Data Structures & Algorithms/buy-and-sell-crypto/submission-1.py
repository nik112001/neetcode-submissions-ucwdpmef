class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        currSum =0
        while r < len(prices):

            if prices[l] < prices[r]:
                sum = prices[r] - prices[l]
                currSum = max(currSum,sum)

            else:
                l = r

            r += 1

        return currSum
