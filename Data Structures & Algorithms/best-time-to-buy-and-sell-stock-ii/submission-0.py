class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        returns = 0

        ln = len(prices)
        for i in range(1,ln):
            print(prices[i-1], prices[i], returns)
            if prices[i] > prices[i-1]:
                returns += abs(prices[i] - prices[i-1])
            

        return returns

