import stack
import queue_class
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adjacencylist = [[] for i  in range(nodes)]
        print(self.adjacencylist)

    def add_edge(self,node1,node2):
        self.adjacencylist[node1].append(node2)
        self.adjacencylist[node2].append(node1)
        print(self.adjacencylist)
    
    def distance_from_source(self,node):
        queue = queue_class.Queue(self.nodes)
        visited = []
        distances = [-1 for i in range(self.nodes)]
        distances[node]=0

        queue.enqueue(node)
        visited.append(node)

        while queue.sizeOfQueue() > 0:
            a = queue.dequeue()
            for n in self.adjacencylist[a]:
                if n not in visited:
                    distances[n] = distances[a] + 1
                    visited.append(n)
                    queue.enqueue(n)
        print(visited)
        print(distances)

graph1 = Graph(9)
graph1.add_edge(0,1)
graph1.add_edge(1,2)
graph1.add_edge(1,3)
graph1.add_edge(3,4)
graph1.add_edge(2,4)
graph1.add_edge(4,5)
graph1.add_edge(5,6)
graph1.add_edge(6,7)
graph1.add_edge(5,8)
graph1.add_edge(7,8)

graph1.distance_from_source(0)