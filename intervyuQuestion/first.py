from typing import List

'''
You are given a string s and an integer array indices of the same length. 
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [''] * len(s)

        for i, index in enumerate(indices):
            shuffled[index] = s[i]

        return ''.join(shuffled)


# example
obj = Solution()
print(obj.restoreString("codeleet", [4,6,5,7,0,2,1,3]))
