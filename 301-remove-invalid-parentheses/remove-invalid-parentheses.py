class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(x):
            bal = 0

            for ch in x:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1

                if bal < 0:
                    return False

            return bal == 0

        level = {s}

        while True:
            valid_strings = [x for x in level if valid(x)]

            if valid_strings:
                return valid_strings

            next_level = set()

            for x in level:
                for i in range(len(x)):
                    if x[i] in '()':
                        next_level.add(x[:i] + x[i + 1:])

            level = next_level