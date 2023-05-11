class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fs = defaultdict(list)
        for path in paths:
            path = path.split()
            for i in range(1,len(path)):
                f = path[i].split("(",1)
                fs[f[1][0:-1]].append(path[0]+'/'+f[0])
        result = []
        for i,x in fs.items():
            if len(x) > 1:
                result.append(x)
        return result