class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        b = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if nums[i] in b:
                return [b[nums[i]], i]
            b[need] = i
            