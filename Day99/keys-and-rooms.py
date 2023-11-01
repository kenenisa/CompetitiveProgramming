class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque([0])
        while q:
            node = q.pop()
            if node in visited:
                continue
            visited.add(node)
            for i in rooms[node]:
                q.append(i)
        return len(visited) == len(rooms)
