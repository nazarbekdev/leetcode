# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeNodes(self, head):
        zero_lst = []
        res = []
        for i in range(len(head)):
            if head[i] == 0:
                zero_lst.append(i)
        print(zero_lst)
        for j in range(len(zero_lst) - 1):
            res.append(sum(head[zero_lst[j]:zero_lst[j + 1]]))
        return res


# example
obj = Solution()
print(obj.mergeNodes([0, 1, 0, 3, 0, 2, 2, 0]))

# this solution wrong in leetcode
