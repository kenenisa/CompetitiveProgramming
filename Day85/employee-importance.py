"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        global imp
        imp = 0
        def findNode(idd):
            for n in employees:
                if n.id == idd:
                    return n
        def dfs(node):
            global imp
            imp += node.importance
            for n in node.subordinates:
                dfs(findNode(n))
        dfs(findNode(id))
        return imp

            
        
        