import random

# The robot's obstacle
rob_obstacles = []

def read_maze_file():
    with open('maze/worlds_crazy_maze.txt') as maze:
        mazelines = maze.readlines()
    return mazelines

def is_position_blocked(x,y):
    """IS POSITION BLOCKED
      ====================
      checks if the coordinate x,y is in the way on one of the obstacles in the robot's obstacles
      - parama : x,y : type -> int(s)
      - return : either True or False
      """
    if x==0 and y==0 or -4 < x < 0 and -4 < y< 0:
        return True
    for i in rob_obstacles:
        if i[0] <= x <= i[0]+4 and i[1] <= y <= i[1]+4:
            return True
    
    return False


def is_path_blocked(curr_x,curr_y, new_x, new_y):
    """IS PATH BLOCKED
     ===================
    
    checks if there is an obstacle between the current position(curr_x,curr_y) of
    ----------------------------------------------------------------------------
    the robot and the future position(new_x,new_y)
    -----------------------------------------------
    
    - param : curr_x,curr_y, new_x, new_y : type -> ints
    - return : either True or False"""
    

    for i in rob_obstacles:
        if (curr_x == new_x and (i[0] <= curr_x <= i[0]+4) and (curr_y >= i[1] >= new_y or
            curr_y <= i[1] <= new_y or curr_y >= i[1]+4 >= new_y or curr_y <= i[1]+4 <= new_y)):
            return True
        elif (curr_y == new_y and (i[1] <= curr_y <= i[1]+4)  and (curr_x >= i[0] >= new_x or
              curr_x <= i[0] <= new_x or curr_x >= i[0]+4 >= new_x or curr_x <= i[0]+4 <= new_x)):
            return True
    
    return False


def generate_obstacles():
    """GENERATE OBSTACLES
       ==================
    Generates obstackes according to the the maze on the textfile
    ------------------------------------------------------------

    -return : world_obstacles: type -> list : description -> list consisting of tuples
    containing the x,y coordinates of the obstacles"""

    mazelines = read_maze_file()

    y_coord = 200
    x_coord = -100
    for lineindex in range(1,len(mazelines)-1):
        mazeline = list(mazelines[lineindex].strip())
        mazeline.pop(0)
        mazeline.pop()
        for grid in mazeline:
            if grid  == "#":
                rob_obstacles.append((x_coord,y_coord-4))
                rob_obstacles.append((x_coord+4,y_coord-4))
                rob_obstacles.append((x_coord,y_coord-8))
                rob_obstacles.append((x_coord+4,y_coord-8))
            x_coord += 8
        y_coord -= 8
        x_coord = -100
    return rob_obstacles