class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        start = 0
        a = [i for i in range(1, n + 1)]

        def backtrack(cur, start):

            if len(cur) == k:
                res.append(cur.copy())
                return

            for i in range(start, len(a)):

                cur.append(a[i])

                backtrack(cur, i + 1)

                cur.pop()

        backtrack([], start)

        return res
        