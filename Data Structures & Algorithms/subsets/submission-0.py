class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = [[], [nums[0]]]

        for j in range(1, len(nums)):
            t = result[:]

            for rest in t:
                result.append(rest + [nums[j]])

        return result
        