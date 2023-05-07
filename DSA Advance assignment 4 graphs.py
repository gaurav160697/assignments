# 1.Breadth First Traversal for a Graph

import collections
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
    
# 2.Depth First Traversal for a Graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2', '3']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')


# 3.Count the number of nodes at given level in a tree using BFS

from collections import deque
  
adj = [[] for i in range(1001)]
  
def addEdge(v, w):

    adj[v].append(w)

    adj[w].append(v)
  
def BFS(s, l):
     
    V = 100
    visited = [False] * V
    level = [0] * V
  
    for i in range(V):
        visited[i] = False
        level[i] = 0
    queue = deque()

    visited[s] = True
    queue.append(s)
    level[s] = 0
    while (len(queue) > 0):
        s = queue.popleft()
        for i in adj[s]:
            if (not visited[i]):
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)
  
    count = 0
    for i in range(V):
        if (level[i] == l):
            count += 1
             
    return count
  
if __name__ == '__main__':
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 5)
    addEdge(2, 7)
    addEdge(2, 6)
  
    level = 2
  
    print(BFS(0, level))
    
    
# 4. count number of trees in a forest. 
 
def Insert_Edge(Graph, u, v): 
    Graph[u].append(v) 
    Graph[v].append(u) 

def Depth_First_Search_Traversal(u, Graph, Check_visited): 
    Check_visited[u] = True
    for i in range(len(Graph[u])): 
        if (Check_visited[Graph[u][i]] == False): 
            Depth_First_Search_Traversal(Graph[u][i], Graph, Check_visited) 

def Count_Tree(Graph, V): 
    Check_visited = [False] * V 
    res = 0
    for u in range(V): 
        if (Check_visited[u] == False): 
            Depth_First_Search_Traversal(u, Graph, Check_visited) 
            res += 1
    return res 

if __name__ == '__main__': 

    V = 7
    Graph = [[] for i in range(V)] 
    Insert_Edge(Graph, 0, 1) 
    Insert_Edge(Graph, 0, 2) 
    Insert_Edge(Graph, 3, 4)
    Insert_Edge(Graph, 4, 5) 
    Insert_Edge(Graph, 5, 6) 
    print(Count_Tree(Graph, V))
    
    
# 5.Detect Cycle in a Directed Graph

from collections import defaultdict
 
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        visited[v] = True
        recStack[v] = True
 
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        recStack[v] = False
        return False
 
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
 
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
 


# **Implement n-Queen’s Problem


def solve_n_queens(n):
    
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_safe(row, col):
        
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q' or \
                    (row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 'Q') or \
                    (row-i >= 0 and col+i < n and board[row-i][col+i] == 'Q') or \
                    (row+i < n and col-i >= 0 and board[row+i][col-i] == 'Q') or \
                    (row+i < n and col+i < n and board[row+i][col+i] == 'Q'):
                return False
        return True

    def solve(row):
       
        if row == n:
            return True

        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                if solve(row + 1):
                    return True
                board[row][col] = '.'

       
        return False

    
    if solve(0):
       
        for row in board:
            print(' '.join(row))
    else:
        print('No solution found.')

solve_n_queens(8)
