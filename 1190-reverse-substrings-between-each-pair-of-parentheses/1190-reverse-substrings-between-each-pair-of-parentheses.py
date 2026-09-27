class Solution:
    def reverseParentheses(self, s: str) -> str:
        lst = []

        for ch in s:
            if ch == ')':
                curr = []

                while lst and lst[-1] != '(':
                    curr.append(lst.pop())

                lst.pop()

                for ch in curr:
                    lst.append(ch)

            else:
                lst.append(ch)

        return "".join(lst)
