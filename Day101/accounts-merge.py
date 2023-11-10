class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        connections = defaultdict(list)
        emailOwners = defaultdict(str)

        for acc in accounts:
            emailOwners[acc[1]] = acc[0]
            for i in range(2,len(acc)):
                connections[acc[1]].append(acc[i])
                connections[acc[i]].append(acc[1])
                emailOwners[acc[i]] = acc[0]
        visited = set()
        def dfs(email,found):
            if email in visited: return 
            visited.add(email)
            found.append(email)
            for e in connections[email]:
                dfs(e,found)
            return found

        result = []
        for e in emailOwners.keys():
            x = dfs(e,[])
            if x:
                x.sort()
                x.insert(0,emailOwners[x[0]])
                result.append(x)
        return result
