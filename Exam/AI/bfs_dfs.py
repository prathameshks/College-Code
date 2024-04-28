class Graph:
    def __init__(self,n:int) -> None:
        self.n = n
        self.mat = [[0 for i in range(n)] for i in range(n)]

    def add_edge(self,start,end):
        self.mat[start][end] = 1
        self.mat[end][start] = 1
    
    def get_mat(self):
        return self.mat
    
    def disp_mat(self):
        print("Adjacency Matrix is As Follows")
        for row in self.mat:
            print(row)
        
    def display_dfs(self,start=0):
        self.visited = [0 for i in range(self.n)]
        print(f"The DFS Traversal Of Graph Starting Form {start} is :")
        self.dfs(start)
        print()
        self.visited = [0 for i in range(self.n)]

    def display_bfs(self,start=0):
        self.visited = [0 for i in range(self.n)]
        self.queue = [start]
        print(f"The BFS Traversal Of Graph Starting Form {start} is :")
        self.bfs()
        print()
        self.visited = [0 for i in range(self.n)]

    def dfs(self,cur):
        print(cur,end=" ")
        self.visited[cur] = 1
        for i in range(self.n):
            if ((self.mat[cur][i]) and (not self.visited[i])):
                self.dfs(i)
    
    def bfs(self):
        if len(self.queue) == 0:
            return None
        cur = self.queue[0]
        self.queue.pop(0)
        print(cur,end=" ")
        self.visited[cur] = 1
        for i in range(self.n):
            if ((self.mat[cur][i]) and (not self.visited[i])):
                self.queue.append(i)
        self.bfs()

def main():
    n = int(input("Enter Number of Nodes:"))
    e = int(input("Enter Number Of Edges:"))

    g = Graph(n)
    for i in range(e):
        start = int(input(f"Enter start of Edge {i+1}:"))
        end = int(input(f"Enter end of Edge {i+1}:"))
        g.add_edge(start,end)
    
    while True:
        print("\n--MENU--\n Enter 1 for BFS\n Enter 2 for DFS\n Enter 3 To display Matrix\n Enter 4 To Exit")
        ch = int(input("Enter choice:"))
        match (ch):
            case 1:
                start = int(input("Enter start node of BFS:"))
                g.display_bfs(start)

            case 2:
                start = int(input("Enter start node of DFS:"))
                g.display_dfs(start)
            
            case 3:
                g.disp_mat()

            case 4:
                print("Thank You!")
                break

            case default:
                print("Invalid Choice")


if __name__ == "__main__":
    main()


"""
sample input 1

4
6
0
1
0
2
1
2
2
0
2
3
3
3

sample input 2

7
6
0
1
0
2
1
3
1
4
4
5
4
6

"""