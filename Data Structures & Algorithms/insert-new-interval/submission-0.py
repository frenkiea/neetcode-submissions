class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.insert(-1, newInterval)
        intervals.sort(key = lambda x: x[0])
        merge = []
        for x in intervals:
            if not merge or merge[-1][1] < x[0]:
                merge.append(x)
            else:
                merge[-1][1] = max(merge[-1][1], x[1])

        return merge 

        