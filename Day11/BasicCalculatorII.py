class Solution:
    def calculate(self, s: str) -> int:
        current = 0
        prev = 0
        op = "+"

        result = 0
        for l in range(len(s)):
            if s[l].isdigit():
                current = current * 10 + ord(s[l]) - ord('0')
            if (not s[l].isdigit() and s[l] != " ") or l == len(s)-1:
                if op == "+":
                    result += current
                    prev = current
                elif op == "-":
                    result -= current
                    prev = -current
                elif op == "*":
                    result = result - prev + (prev*current)
                    prev = prev*current
                elif op == "/":
                    result = result - prev + (int(prev/current))
                    prev = int(prev/current)
                op = s[l]
                current = 0
        return result
