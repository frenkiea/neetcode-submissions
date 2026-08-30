class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        def checkd(arr):
            dem = 0
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    dem += 1
            return True if dem == len(arr) - 1 else False
        if checkd(prices) == True:
            return 0
        for i in range(len(prices)):
            profit = max(profit, max(prices[i + 1 :], default=0) - prices[i])
        return profit