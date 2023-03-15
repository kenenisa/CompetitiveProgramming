def superDigit(n, k):
    # Write your code here
    # @lru_cache(maxsize=20)
    def super_digit(n,f=True):
        if len(n) == 1: return n
        s = 0
        for i in n:
            s += int(i)
        if f:
            return super_digit(str(s))
        return s
    return super_digit(str(k*super_digit(n,False)))