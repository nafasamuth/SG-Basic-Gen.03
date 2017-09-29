class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def getVertices(self):
        #mengembalikan semua vertex pada graf
        return list(self.__graph_dict.keys())

    def getEdges(self):
        #mengembalikan semua sisi pada graf
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        #menghasilkan semua sisi pada graf
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def __getitem__(self,vertex):
      return self.__graph_dict[vertex]

def dfs(graph,start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.append(vertex)
            for neighbour in graph[vertex]:
                stack.append(neighbour)
    return visited

def bfs(graph,start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            for neighbour in graph[vertex]:
                queue.append(neighbour)
    return visited


g = {1: set([3, 2]),
         2: set([1,4, 5]),
         3: set([1,6,7]),
         4: set([2,8]),
         5: set([2, 8]),
         6: set([3,8]),
         7: set([3,8]),
         8: set([4,5,6,7])}

graph = Graph(g)

# for i in range(6):
#     graph.add_vertex(i)

# print(graph.getVertices())

# graph.add_edge({1,2})

# print(graph.getEdges())

print(graph)
print(dfs(graph,1))
print(bfs(graph,1))
a=[1,2,3]
b=[2,3,4]

for i in a:
    if i not in b:
        print(i)

