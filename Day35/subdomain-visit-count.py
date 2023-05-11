class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        df = defaultdict(int)
        for cp in cpdomains:
            rep,domain = cp.split()
            d = domain.split('.')
            s = ''
            for i in range(len(d)-1,-1,-1):
                if s:
                    s = d[i] + '.' + s
                else:
                    s = d[i]
                df[s] += int(rep)
        result = []
        for item,rep in df.items():
            result.append(str(rep) + ' ' + item)
        return result