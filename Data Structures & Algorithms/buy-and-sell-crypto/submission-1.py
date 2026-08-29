class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t = []
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

            for j in range(i + 1, len(prices)):

                if prices[j] > prices[i]:
                    t.append(prices[j])
                    profit = max(profit, max(t) - prices[i])
            
            t = []

        return profit
        