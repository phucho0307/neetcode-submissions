class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(list)
        seen = set()
        for nodes in edges:
            k,v =  nodes[0], nodes[1]
            hmap[k].append(v)
            hmap[v].append(k)
        def dfs(node):
            if node in seen:
                return
 
        
            seen.add(node)
            for point in hmap[node]:
                dfs(point)
        
        count = 0
        for node in range(n):  
            if node not in seen: 
                dfs(node)
                count +=1
        return count
