from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        deffect = 0
        for i in range(len(intervals) - 1):
            if intervals[i][-1] != intervals[i + 1][0]:
                print(intervals[i][-1], ' ', intervals[i + 1][0])
                deffect += 1
        return deffect


# example
obj = Solution()
print(obj.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))

# in progress
