class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def separate(word:str):
            p = []
            for i in word:
                if not p or i in string.ascii_uppercase:
                    p.append([i])
                else:
                    p[-1].append(i)
                    
            return p
        p = separate(pattern)
        result = [False] * len(queries)
        for i in range(len(queries)):
            w = separate(queries[i])
            ax = w[0][0] in string.ascii_lowercase
            bx = p[0][0] in string.ascii_lowercase
            if ax ^ bx:
                if ax: w.pop(0)
                if bx: p.pop(0)
            if len(w) == len(p):
                valid = True
                for j in range(len(w)):
                    if len(w[j]) >= len(p[j]) and (w[j][0] in string.ascii_lowercase or w[j][0] == p[j][0]):
                        a = Counter(w[j])
                        b = Counter(p[j])
                        v = True
                        for k in string.ascii_lowercase:
                            if a[k] < b[k]:
                                v = False
                                break
                        if v: continue
                    valid = False
                    break
                result[i] = valid
        return result


        
