
class Solution:
    def is_pair(self, open, close):
        if open == "(" and close != ")":
            return False

        elif open == "{" and close != "}":
            return False

        elif open == "(" and close != ")":
            return False

        else:
            return True

    def isValid(self, s: str) -> bool:
        stack = []
        index = 0
        is_balanced = True

        while is_balanced and index < len(s):
            paren = s[index]

            if paren in "({[":
                stack.append(paren)

            else:
                if stack == []:
                    is_balanced = False

                else:
                    open = stack.pop()
                    if not self.is_pair(open, paren):
                        is_balanced = False

            index += 1

        if stack == [] and is_balanced:
            print("true")

        else:
            print("f")

s = Solution()
s.isValid("(]")


