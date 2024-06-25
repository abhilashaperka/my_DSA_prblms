#find center of a star graph
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counts=[]
        for e in edges:
            if e[0] in counts:
                return e[0]
            if e[1] in counts:
                return e[1]
            counts.append(e[0])
            counts.append(e[1])
