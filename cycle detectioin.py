from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self,s):
        vis = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        vis[s] = True

        while queue:
            s = queue.pop(0)
            print(s,end = " ")
            for i in self.graph[s]:
                if vis[i] == False:
                    queue.append(i)
                    vis[i] = True
                elif vis[i]:
                    print("Cycle found")
                    return


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1,3)


g.BFS(2)