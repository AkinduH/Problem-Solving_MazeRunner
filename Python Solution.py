#Define the available directions for each cell
last_four_digits = [
    [0,1,1,0],[0,1,0,1],[0,1,1,1],[0,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[0,1,0,0],[0,1,1,1],[0,1,0,1],[0,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],
    [1,0,1,0],[0,1,0,0],[1,1,0,1],[0,0,0,1],[1,0,1,0],[0,1,0,0],[1,1,0,1],[0,1,1,1],[1,0,1,1],[0,1,0,0],[0,1,0,1],[1,1,0,1],[0,0,0,1],[1,0,1,0],
    [1,1,1,0],[0,1,1,1],[0,0,0,1],[0,1,1,0],[1,0,0,1],[0,1,1,0],[0,0,0,1],[1,0,1,0],[1,1,0,0],[0,1,0,1],[0,1,0,1],[0,0,1,1],[0,1,1,0],[1,0,1,1],
    [1,0,1,0],[1,0,1,0],[0,1,0,0],[1,1,1,1],[0,1,0,1],[1,0,0,1],[0,1,0,0],[1,1,0,1],[0,0,0,1],[0,1,1,0],[0,1,0,1],[1,0,0,1],[1,0,1,0],[1,0,1,0],
    [1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[0,1,1,0],[0,1,0,1],[0,1,0,1],[0,0,1,1],[0,1,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1],[1,0,0,1],[1,0,1,0],
    [1,0,1,0],[1,0,1,0],[1,0,0,0],[1,0,1,0],[1,0,1,0],[0,1,1,0],[0,0,0,1],[1,0,1,0],[1,0,1,0],[0,1,1,0],[1,0,1,1],[0,1,1,0],[0,0,1,1],[1,0,0,0],
    [1,0,0,0],[1,1,1,0],[0,0,1,1],[1,0,1,0],[1,0,1,0],[1,0,1,0],[0,1,1,0],[1,1,0,1],[1,0,0,1],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[0,0,1,0],
    [0,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,1,1,0],[0,0,0,1],[0,0,1,0],[1,0,0,0],[1,1,1,0],[1,0,0,1],[1,0,1,0],[1,0,1,0],
    [1,0,1,0],[1,0,0,0],[1,1,1,0],[1,0,0,1],[1,0,1,0],[1,1,0,0],[1,0,0,1],[0,1,1,0],[1,0,0,1],[0,0,1,0],[1,0,1,0],[0,1,1,0],[1,1,0,0],[1,0,1,1],
    [1,1,1,0],[0,1,0,1],[1,1,0,1],[0,0,0,1],[1,1,0,0],[0,1,0,1],[0,0,1,1],[1,1,0,0],[0,1,0,1],[1,1,0,1],[1,0,1,1],[1,0,1,0],[0,0,1,0],[1,0,1,0],
    [1,0,0,0],[0,0,1,0],[0,1,1,0],[0,1,0,1],[0,1,0,1],[0,0,1,1],[1,1,1,0],[0,0,1,1],[0,1,1,0],[0,1,0,1],[1,0,0,1],[1,0,1,0],[1,0,1,0],[1,0,1,0],
    [0,1,1,0],[1,0,1,1],[1,0,1,0],[0,1,1,0],[0,0,1,1],[1,1,0,0],[1,0,0,1],[1,0,1,0],[1,1,0,0],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,1,0,0],[1,1,1,1],
    [1,0,1,0],[1,1,0,0],[1,0,0,1],[1,0,1,0],[1,1,0,0],[0,1,1,1],[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,1,0,1],[1,0,0,1],[1,1,0,0],[0,0,0,1],[1,0,1,0],
    [1,1,0,0],[0,1,0,1],[0,1,0,1],[1,1,0,1],[0,0,1,1],[1,1,0,0],[0,1,0,1],[0,1,0,1],[1,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[1,0,0,1]
]

#Creating the maze
maze = []
row = 0
for i in range(14):
    maze.append([])
    for j in range(14):
        x, y = i, j
        element = [(x, y)]
        element.extend(last_four_digits[row])
        row += 1
        maze[i].append(element)


# Define the starting cell
start=(maze[2][0])
print('Start at ( 2 , 0 )')
# Define lists for explored cells and front cells
exploredCells_stack=[start]
frontClells_stack=[None,start]
# Define lists to keep track of directions and child cells
childCell=[]
Direction_list=[]

while len(frontClells_stack)>0:
    currCell=frontClells_stack[-1]
    # Check if the current cell is in the goal
    if currCell[0]==(11,13):
        for x in Direction_list:
            print(x,end=' ')
        print(f"Leaving at ( {currCell[0][0]} , {currCell[0][1]} )")
        break
    # Determine the accessible neighboring cells based on walls
    if currCell[1]==1:North_Cell=maze[currCell[0][0]-1][currCell[0][1]]
    if currCell[2]==1:East_Cell=maze[currCell[0][0]][currCell[0][1]+1]
    if currCell[3]==1:South_Cell=maze[currCell[0][0]+1][currCell[0][1]]
    if currCell[4]==1:West_Cell=maze[currCell[0][0]][currCell[0][1]-1]

    # Explore the accessible neighboring cells
    if currCell[1]==1 and North_Cell not in exploredCells_stack:
        Direction_list.append('North')
        childCell=North_Cell
        maze[currCell[0][0]][currCell[0][1]][1]=0
    elif currCell[2]==1 and East_Cell not in exploredCells_stack:
        Direction_list.append('East')
        childCell=East_Cell
        maze[currCell[0][0]][currCell[0][1]][2]=0
    elif currCell[3]==1 and South_Cell not in exploredCells_stack:
        Direction_list.append('South')
        childCell=South_Cell
        maze[currCell[0][0]][currCell[0][1]][3]=0
    elif currCell[4]==1 and currCell[4]==1 and West_Cell not in exploredCells_stack:
        Direction_list.append('West')
        childCell=West_Cell
        maze[currCell[0][0]][currCell[0][1]][4]=0
        
    # Handle when the current cell cannot be explored further
    else:
         if currCell[1]==1:childCell=North_Cell
         elif currCell[2]==1:childCell=East_Cell
         elif currCell[3]==1:childCell=South_Cell
         elif currCell[4]==1:childCell=West_Cell
         if childCell[1]==frontClells_stack[-2][1]:
            for x in Direction_list:
                print(x,end=' ')
            print(f"Stuck at ( {currCell[0][0]} , {currCell[0][1]} )")
            print(f"Back to ( {childCell[0][0]} , {childCell[0][1]} )")
            Direction_list=[]

         else:
             print(f"Stuck at ( {currCell[0][0]} , {currCell[0][1]} )")
             print(f"Back to ( {childCell[0][0]} , {childCell[0][1]} )")


    exploredCells_stack.append(childCell)
    frontClells_stack.append(childCell)