class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    
        graph = {}
        
        def build_graph():  
            for [s,e],val in zip(equations,values):    
                if s in graph:
                    graph[s].append((e,val))
                else:
                    graph[s] = [(e,val)]
                    
                if e in graph:
                     graph[e].append((s,1/val))
                else:
                    graph[e] = [(s,1/val)]
                    
        def findPath(s,e):
            if s not in graph or e not in graph:
                return -1.0
            
            if s == e:
                return 1.0
            
            visited = set()
            
            stack = []
            
            stack.append((s,1.0))
            
            while stack:
                i,prod = stack.pop()
                
                if i == e:
                    return prod
                visited.add(i)
                for neighbour,val in graph[i]:
                    if neighbour not in visited:
                        stack.append((neighbour,prod*val))
                        visited.add(neighbour)
            return -1.0
        
        build_graph()
        ans = []
        for s,e in queries:
            ans.append(findPath(s,e))
        return ans
                    
            
                
        
