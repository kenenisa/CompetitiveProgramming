class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        buckets = 0
        i = 0
        while i < n:
            if street[i] == '.': 
                i += 1
                continue
            l = i - 1
            r = i + 1
            if r <= n-1:
                if street[r] == '.':
                    if r + 1 <= n-1:
                        if street[r+1] == '.':
                            buckets += 1
                            i += 2
                            continue
                        else:
                            buckets += 1
                            i += 3
                            continue
                    else:
                        buckets += 1
                        i +=1
                        continue
            if l >= 0:
                if street[l] == '.':
                    buckets += 1
                    i+=1
                    continue
                else:
                    return -1
            else:
                return -1
        return buckets