from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lst_s = list(s)  # ['a', 'a', 'b']
        polindr = []
        if len(lst_s) == 1:
            polindr.append(lst_s)
            return polindr
        else:
            for i in range(len(lst_s)-1):
                if lst_s[i] == lst_s[i+1]:
                    polindr.append([lst_s[i] + lst_s[i+1]])
                else:
                    if len(lst_s) == 2:
                        polindr.append([lst_s[i], lst_s[i+1]])
                    else:
                        polindr.append(lst_s[i+1])

        return polindr


obj = Solution()
print(obj.partition("baab"))

# in progress
