class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        n=len(chars)
        pos = 0
        while i < n:
            current = chars[i]
            count = 0
            at = pos
            while i < n and current == chars[i]:
                # print(i,chars[i])
                count += 1
                i += 1
            chars[at] = current
            pos += 1
            if count > 1:
                count = str(count)
                for c in range(len(count)):
                    chars[at + c + 1] = count[c]
                    pos += 1
        return pos