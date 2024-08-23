from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        one_rooms = 0
        two_rooms = 0
        for num in nums:
            if num < 10:
                one_rooms += num
            else:
                two_rooms += num
        if two_rooms != one_rooms:
            return True
        else:
            return False


# example
obj = Solution()
print(obj.canAliceWin([1, 2, 3, 4, 10]))
