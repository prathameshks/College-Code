def copy_matrix(mat):
    ans = []
    for i in mat:
        temp = []
        for j in i:
            temp.append(j)
        ans.append(temp)
    return ans

def print_state(title,state,h,g=0):
    print(title)
    for row in state:
        for elmt in row:
            print(elmt,end=" ")
        print()
    print(f"g={g}, h={h}, f={g+h}\n")

# get input
def get_input(msg):
    print(msg)
    ans = []
    ans.append(input().split(" "))
    ans.append(input().split(" "))
    ans.append(input().split(" "))
    return ans

def get_f(node):
    return node.f_score

def compare_matrix(a,b):
    for i in range(3):
        for j in range(3):
            if(a[i][j] != b[i][j]):
                return False
    return True

class Node:
    data = [[]]
    level = 0
    f_score = 0
    
    def __init__(self,data,level = 0,f_score= 0) -> None:
        self.data = data
        self.level = level
        self.f_score = f_score
        
    def get_blank(self):
        for i in range(3):
            for j in range(3):
                if self.data[i][j] == '_':
                    return [i,j]

        print("No Underscore Found")
        exit()
            
    def generate_child(self):
        i,j = self.get_blank()
        
        children = []
        
        # up
        if(i != 0):
            mat1 = copy_matrix(self.data)
            mat1[i-1][j],mat1[i][j] = mat1[i][j],mat1[i-1][j]
            children.append(mat1)
            
        # down
        if(i != 2):
            mat2 = copy_matrix(self.data)
            mat2[i+1][j],mat2[i][j] = mat2[i][j],mat2[i+1][j]
            children.append(mat2)
            
        # left
        if(j != 0):
            mat3 = copy_matrix(self.data)
            mat3[i][j-1],mat3[i][j] = mat3[i][j],mat3[i][j-1]
            children.append(mat3)
            
        # right
        if(j != 2):
            mat4 = copy_matrix(self.data)
            mat4[i][j+1],mat4[i][j] = mat4[i][j],mat4[i][j+1]
            children.append(mat4)
            
        return children
    
    def p(self):
        print(self.data)
        print(self.level)
        print(self.f_score)
        
    def h(self,goal):
        h_score = 0
        for i in range(3):
            for j in range(3):
                if(self.data[i][j] != '_' and self.data[i][j] != goal[i][j]):
                    h_score += 1
        
        return h_score
    


    

def main():
    start = get_input("Enter Start Matrix")
    goal = get_input("Enter Goal Matrix:")
    
    start_node = Node(start)
    visited = [tuple(map(tuple, start))]
    
    arr = [start_node]
    while True:
        curr = arr.pop(0)
        h_val = curr.h(goal)
        curr.f_score = curr.level + h_val
        if( h_val == 0):
            print_state("Goal State Reached",curr.data,h_val,curr.level)
            return
        
        print(len(visited))
        print(len(arr))
        print_state("Choosing State",curr.data,h_val,curr.level)
        
        children = curr.generate_child()
        for child in children:
            if tuple(map(tuple, child)) not in visited:
                visited.append(tuple(map(tuple, child)))
                temp_child = Node(child,curr.level+1)
                temp_child.f_score = temp_child.level + temp_child.h(goal)
                arr.append(temp_child)
        
        if(arr == []):
            print("No Solution Found")
            return
        
        arr.sort(key=get_f)


 
"""
1 2 3
4 5 6
7 8 _
1 2 3
4 5 6
7 _ 8 


1 2 3
4 5 6
7 8 _
1 2 3
6 5 4
7 _ 8 
"""

main()
