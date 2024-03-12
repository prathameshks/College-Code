# N-Queens Problem
ans = [[]]
def printBoard(arr):
    for a in arr:
        for b in a:
            if(b): print('Q', end=" ")
            else: print('.',end=" ")
        print()

def copy(board,n):
    global ans
    for i in range(n):
        for j in range(n):
            ans[i][j] = board[i][j]

def isSafe(board,x,y,n):
    # in row
    j = 0
    while(j<n):
        if(board[x][j] == 1):
            return False
        j+=1

    # col above
    i = x-1
    while(i>=0):
        if(board[i][y] == 1):
            return False
        i-=1
        
    # diagonal top left
    i = x-1
    j = y-1
    while(i>=0 and j >= 0):
        if(board[i][j] == 1):
            return False
        i-=1
        j-=1

    # diagonal top right
    i = x-1
    j = y+1
    while(i>=0 and j < n):
        if(board[i][j] == 1):
            return False
        i-=1
        j+=1

    return True

def solve(row,  board, n,j=0):
    if row >= n:
        if(j==n-1):
            print("Solution:")
            printBoard(board)
            print("\n")
        copy(board, n)
        return

    for j in range(n):  # Iterate over columns only
        if isSafe(board, row, j, n):
            # put queen
            board[row][j] = 1
            # solve
            solve(row + 1,  board, n,j)
            # backtrack
            board[row][j] = 0

def main(n):
    global ans
    board = [[0 for i in range(n)] for i in range(n)]
    ans = [[0 for i in range(n)] for i in range(n)]

    solve(0,board,n)

    print("Final Solution Is:")
    printBoard(ans)

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    main(n)