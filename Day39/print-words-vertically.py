class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        longest = len(max(s,key=len))
        result = []
        for i in range(longest):
            item = []
            for word in s:
                item.append(word[i] if i < len(word) else " ")
            result.append("".join(item).rstrip())
        return result