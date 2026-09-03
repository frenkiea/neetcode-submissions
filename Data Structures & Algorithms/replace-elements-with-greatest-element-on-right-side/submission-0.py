class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        t = []
        for i in range(len(arr)):
            if i + 1 > len(arr) - 1:
                t.append(-1)
            else:
                t.append(max(arr[i + 1:]))
        return t