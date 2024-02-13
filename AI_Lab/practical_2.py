from copy import deepcopy

def print_state(title,state,h,g=0):
    print(title)
    for row in state:
        for elmt in row:
            print(elmt,end=" ")
        print()
    print(f"g={g}, h={h}, f={g+h}\n")

def compare(initial,goal):
    diff = 0
    for i in range(3):
        for j in range(3):
            if(initial[i][j] != goal[i][j]):
                diff+=1
    return diff

def identify_blank(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j] == 0):
                return (i,j)

def move_left(state,i,j):
    if(j!=0):
        state[i][j], state[i][j-1] = state[i][j-1], state[i][j]
        return state
    return None

def move_down(state,i,j):
    if(i!=2):
        state[i][j], state[i+1][j] = state[i+1][j], state[i][j]
        return state
    return None

def move_right(state,i,j):
    if(j!=2):
        state[i][j], state[i][j+1] = state[i][j+1], state[i][j]
        return state
    return None

def move_up(state,i,j):
    if(i!=0):
        state[i][j], state[i-1][j] = state[i-1][j], state[i][j]
        return state
    return None

def solve(start,goal):
    


a = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]

g = [
    [2,8,1],
    [0,4,3],
    [7,6,5]
]
    
solve(a,g)
