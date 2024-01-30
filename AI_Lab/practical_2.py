import copy

def compare(initial,goal):
    diff = 0
    for i in range(3):
        for    j in range(3):
            if(initial[i][j] != goal[i][j]):
                diff+=1
    return diff

def identify_blank(state):
    for i in range(3):
        for    j in range(3):
            if(state[i][j] == 0):
                return (i,j)
            
def move_left(state,i,j):
    if(j!=0):
        state[i][j] = state[i][j-1]
        state[i][j-1] = 0
        return state
    return None

def move_down(state,i,j):
    if(i!=2):
        state[i][j] = state[i+1][j]
        state[i+1][j] = 0
        return state
    return None

def move_right(state,i,j):
    if(j!=2):
        state[i][j] = state[i][j+1]
        state[i][j+1] = 0
        return state
    return None

def move_up(state,i,j):
    if(i!=0):
        state[i][j] = state[i-1][j]
        state[i-1][j] = 0
        return state
    return 

def a_star(initial,goal):
    diff = compare(initial,goal)
    i,j = identify_blank(initial)
    
    min_diff = 10
    min_temp = copy.deepcopy(initial)

    # move up
    up_state = copy.deepcopy(initial)
    move_up(up_state,i,j)
    if(up_state):
        d = compare(up_state,goal)
        if(d < min_diff):
            min_diff = d
            min_temp = copy.deepcopy(up_state)


    # move down
    down_state = copy.deepcopy(initial)
    move_down(down_state,i,j)
    if(down_state):
        d = compare(down_state,goal)
        if(d < min_diff):
            min_diff = d
            min_temp = copy.deepcopy(down_state)


    # move right
    right_state = copy.deepcopy(initial)
    move_right(right_state,i,j)
    if(right_state):
        d = compare(right_state,goal)
        if(d < min_diff):
            min_diff = d
            min_temp = copy.deepcopy(right_state)


    # move left
    left_state = copy.deepcopy(initial)
    move_left(left_state,i,j)
    if(left_state):
        d = compare(left_state,goal)
        if(d < min_diff):
            min_diff = d
            min_temp = copy.deepcopy(left_state)

    print('up_state')
    print(up_state)
    print('down_state')
    print(down_state)
    print('right_state')
    print(right_state)
    print('left_state')
    print(left_state)


    print('diff')
    print(diff)
    
    print('min_diff')
    print(min_diff)
    
    print('min_temp')
    print(min_temp)
    
    
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
    
a_star(a,g)
