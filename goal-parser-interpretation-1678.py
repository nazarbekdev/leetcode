"""Solution 1"""


class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        if command.endswith('(al)'):
            for i in range(len(command)-3):
                if command[i] == 'G':
                    s += 'G'
                elif command[i] == '(' and command[i+1] == ')':
                    s += 'o'
                elif command[i] == '(' and command[i+1] == 'a':
                    s += 'al'
        elif command.endswith('()'):
            for i in range(len(command)-1):
                if command[i] == 'G':
                    s += 'G'
                elif command[i] == '(' and command[i+1] == ')':
                    s += 'o'
                elif command[i] == '(' and command[i+1] == 'a':
                    s += 'al'
        elif command.endswith('G'):
            for i in range(len(command)):
                if command[i] == 'G':
                    s += 'G'
                elif command[i] == '(' and command[i+1] == ')':
                    s += 'o'
                elif command[i] == '(' and command[i+1] == 'a':
                    s += 'al'
        return s


# example
obj = Solution()
print(obj.interpret('(al)G(al)()()G'))

""" Solution 2 """


class Solution:
    def interpret(self, command: str) -> str:
        s = command.replace('()', 'o').replace('(al)', 'al')
        return s


# example
obj = Solution()
print(obj.interpret('(al)G(al)()()G'))
