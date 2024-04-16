def print_menu():
    print("--MENU--")
    print("1. Selection Sort")
    print("2. Prim's Minimum Spanning Tree Algorithm")
    print("9. exit")

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

def print_2D(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print()

def selection_sort(list):
    for i in range(len(list)):
        t = i
        for j in range(i+1, len(list)):
            if list[t] > list[j]:
                t = j
        temp = list[i]
        list[i] = list[t]
        list[t] = temp
    return list

def prims_algorithm():
    n = int(input("Enter Number of Nodes: "))
    mat = [[0]*n for _ in range(n)]
    m = int(input("Enter Number of Edges: "))
    for i in range(m):
        print("Enter Details of Edge "+str(i+1)+" as start end weight")
        start, end, weight = map(int, input().split())
        mat[start][end] = weight
        mat[end][start] = weight
    print_2D(mat)

    # Prim's algorithm
    visited = [0]*n
    visited[0] = 1
    tree = []
    while len(tree) < n-1:
        min = float('inf')
        x = 0
        y = 0
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if ((not visited[j]) and mat[i][j]):
                        if min > mat[i][j]:
                            min = mat[i][j]
                            x = i
                            y = j
        tree.append((x, y, min))
        visited[y] = 1
    for edge in tree:
        print(edge)

while True:
    print_menu()
    ch = int(input("Enter Your Choice(0 to Display Menu):"))
    if ch == 0:
        print_menu()
        ch = int(input("Enter Your Choice:"))
    if ch == 1:
        n = int(input("Enter Number of Elements:"))
        l = list(map(int, input("Enter Numbers:").split()))
        print("Original List ", end="")
        print_list(l)
        newl = selection_sort(l)
        print("List After Selection Sort ", end="")
        print_list(newl)
    elif ch == 2:
        prims_algorithm()
    elif ch == 9:
        print("Thank You")
        break
    else:
        print("Invalid Input")

"""
0 2 3
1 2 9
1 3 4
2 3 2
2 4 6
3 4 1
"""