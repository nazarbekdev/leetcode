from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_height = sorted(heights, reverse=True)
        sorted_names = []
        for i in sorted_height:
            sorted_names.append(names[heights.index(i)])
        return sorted_names


# example
obj = Solution()
print(obj.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
