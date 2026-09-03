class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        start = 0
        
        def backtrack(cur, start):
            if sum(cur) == target:
                res.append(cur.copy())
                return

            for i in range(start, len(nums)):
                cur.append(nums[i])
                if sum(cur) <= target:
                    backtrack(cur, i)
                
                cur.pop()
                
        backtrack([], 0)
        
        return res




        