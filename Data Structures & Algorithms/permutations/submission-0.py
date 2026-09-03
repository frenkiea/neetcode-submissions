class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        t = []
        used = [False] * len(nums)
        def backtrack(cur):
            
            if len(cur) == len(nums):
                t.append(cur[:])
                return
            
            for i in range(len(nums)):

                if used[i]:
                    continue
                
                used[i] = True
                cur.append(nums[i])

                backtrack(cur)

                cur.pop()
                used[i] = False
            
        backtrack([])
        
        return t
        