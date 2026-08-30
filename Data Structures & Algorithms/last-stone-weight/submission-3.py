class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def count(arr):
            dem = 0

            for i in range(len(arr)):

                if arr[i] == 0:
                    dem += 1

            if dem >= len(arr) - 1:
                return True
            else:
                return False

        w1 = 0
        w2 = 0

        while count(stones) != True:
            new_stones = sorted(stones)
            a1, a2 = new_stones[len(stones) - 1], new_stones[len(stones) - 2]
            dem = 0
            i = 0

            if a1 == a2:
                while dem < 2:
                    if stones[i] == a1:
                        dem += 1
                        stones[i] = 0
                    i += 1

            else:
                for j in range(len(stones)):
                    if stones[j] == a1:
                        w1 = j
                    if stones[j] == a2:
                        w2 = j

                stones[w1] =  stones[w1] - stones[w2]
                stones[w2] = 0

        if stones == [0] * len(stones):
            return 0
        else:
            return sum(stones)
        