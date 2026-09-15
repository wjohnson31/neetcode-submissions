class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removals = 0
        prev = intervals[0][1]
        for x, y in intervals[1:]:
            if x < prev:
                removals += 1
                prev = min(y, prev)

            else:
                prev = y
        return removals