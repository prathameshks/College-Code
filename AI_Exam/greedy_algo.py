def print_list(arr):
    print(' '.join(str(i) for i in arr))

def print_2D(arr):
    for row in arr:
        print(' '.join(str(i) for i in row))
    print()

def selection_sort(lst):
    for i in range(len(lst)):
        t = i
        for j in range(i+1, len(lst)):
            if lst[t] > lst[j]:
                t = j
        lst[i], lst[t] = lst[t], lst[i]
    return lst

def prims_algorithm():
    n = int(input("Enter Number of Nodes: "))
    mat = [[0]*n for _ in range(n)]
    m = int(input("Enter Number of Edges: "))
    for i in range(m):
        print(f"Enter Details of Edge {i+1} as start end weight")
        start, end, weight = map(int, input().split())
        mat[start][end] = weight
        mat[end][start] = weight
    print_2D(mat)
    vis = [0]*n
    tree = [[0]*3 for _ in range(n-1)]
    sumw = 0
    for i in range(n):
        if vis[i] == 1:
            sv, ev, wv = 0, 0, 999
            flag = False
            for j in range(n):
                if mat[i][j] > 0 and mat[i][j] < wv and vis[j] != 1:
                    wv = mat[i][j]
                    sv = i
                    ev = j
                    flag = True
            if flag:
                vis[ev] = 1
                tree[sumw][0] = sv
                tree[sumw][1] = ev
                tree[sumw][2] = wv
                sumw += 1
            else:
                break
    print("Tree is :")
    print_2D(tree)

while True:
    print("--MENU--")
    print("1. Selection Sort")
    print("2. Prim's Minimum Spanning Tree Algorithm")
    print("9. exit")
    ch = int(input("Enter Your Choice(0 to Display Menu): "))
    if ch == 1:
        n = int(input("Enter Number of Elements: "))
        lst = list(map(int, input("Enter Numbers: ").split()))
        print("Original List ", end='')
        print_list(lst)
        new_lst = selection_sort(lst)
        print("List After Selection Sort ", end='')
        print_list(new_lst)
    elif ch == 2:
        prims_algorithm()
    elif ch == 9:
        print("Thank You")
        break
    else:
        print("Invalid Input")
