import queue_class
import stack
class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adjacencylist = [[] for i  in range(nodes)]
        print(self.adjacencylist)

    def add_edge(self,node1,node2):
        self.adjacencylist[node1].append(node2)
        self.adjacencylist[node2].append(node1)
        print(self.adjacencylist)
    
    def BFS(self,node):
        queue = queue_class.Queue(self.nodes)
        visited = []

        queue.enqueue(node)
        visited.append(node)

        while queue.sizeOfQueue() > 0:
            a = queue.dequeue()
            for n in self.adjacencylist[a]:
                if n not in visited:
                    visited.append(n)
                    queue.enqueue(n)
        print(visited)
    
    def DFS(self,start):
        stack1 = stack.Stack(self.nodes)
        visited = []
        stack1.push(start)
        while stack1.isEmpty() == False:
            add_visited = stack1.pop()
            visited.append(add_visited)
            for node in self.adjacencylist[add_visited]:
                if node not in visited and not stack1.check_is_there(node):
                    stack1.push(node)
        print(visited)




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

graph1.BFS(0)
graph1.DFS(0)
graph1.BFS(0)
