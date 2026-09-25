class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expr():
            nonlocal i
            res = set()

            while True:
                res |= parse_term()

                if i == len(expression) or expression[i] == '}':
                    break

                i += 1

            return res

        def parse_term():
            nonlocal i
            res = {""}

            while i < len(expression) and expression[i] not in ',}':
                if expression[i] == '{':
                    i += 1
                    cur = parse_expr()
                    i += 1
                else:
                    cur = {expression[i]}
                    i += 1

                res = {a + b for a in res for b in cur}

            return res

        i = 0
        return sorted(parse_expr())