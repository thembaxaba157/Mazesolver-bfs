import maze.obstacles as mazeobs
obstacles = []
visited_nodes = []
edge = ''
init_direction = ''
#not gonna be used
init_position_x = 0
init_position_y = 0
gridsize = 0
min_y, max_y = -200, 200
min_x, max_x = -100, 100



def mazerun_message(robot_name):
    """MAZERUN MESSAGE
    ===================
    
    - Returns the message to be displayed after the robot reaches the specified edge"""

    global edge

    if edge == 'top':
        return ''+robot_name+': I am at the top edge.'
    elif edge == 'left':
        return ''+robot_name+': I am at the left edge.'
    elif edge == 'right':
        return ''+robot_name+': I am at the right edge.'
    elif edge == 'bottom':
        return ''+robot_name+': I am at the bottom edge.'


def change_direction(init_node,final_node,direction):
    """ CHANGE DIRECTION
        ================

        -Changes the diretion of the robot when it turns
        - Returns : the direction it must face and turn it must take
        """
    
    if direction == 'forward' and init_node[0]>final_node[0]:
        return 'left','left'
    elif direction == 'forward' and init_node[0]<final_node[0]:
        return 'right','right'
    elif direction == 'back' and init_node[0]>final_node[0]:
        return 'left','right'
    elif direction == 'back' and init_node[0]<final_node[0]:
        return 'right','left'
    
    elif direction == 'right' and init_node[1]>final_node[1]:
        return 'back','right'
    elif direction == 'right' and init_node[1]<final_node[1]:
        return 'forward','left'
    elif direction == 'left' and init_node[1]>final_node[1]:
        return 'back','left'
    elif direction == 'left' and init_node[1]<final_node[1]:
        return 'forward','right'


def get_movement(steps,init_node,final_node,direction):
    """GET MOVEMENT
       ===========
       
        -Gets the movement command the robot must execute until it changes 
         direction or reaches the edge
        - returns: the command either forward or back and the number of steps """
        
   
    if direction == 'forward' and final_node[1]>=init_node[1]:
        return f'forward {steps}'
    elif direction == 'forward' and init_node[1]>=final_node[1]:
        return f'back {steps}'
    elif direction == 'right' and final_node[0]>=init_node[0]:
        return f'forward {steps}'
    elif direction == 'right' and init_node[0]>=final_node[0]:
        return f'back {steps}'
    elif direction == 'back' and final_node[1]<=init_node[1]:
        return f'forward {steps}'
    elif direction == 'back' and init_node[1]<=final_node[1]:
        return f'back {steps}'
    elif direction == 'left' and final_node[0]<=init_node[0]:
        return f'forward {steps}'
    elif direction == 'left' and init_node[0]<=final_node[0]:
        return f'back {steps}'

def get_moves(path,direction):
    """GET MOVES
       =========
       
       - Returns: a list of commands the robot must execute to reach the edge"""
    steps = 0
    moves = []
    init_node = path[0]
    final_node = path[1]
    movement = ''
    turn = ''
    for i in range(len(path)-1):

        if direction == 'forward' or direction == 'back':
            if path[i][0] == path[i+1][0]:
                steps += abs(path[i][1]-path[i+1][1])
                final_node = path[i+1]

            else:
                if steps>0:
                    movement = get_movement(steps,init_node,final_node,direction)
                
                    moves.append(movement)
                    direction,turn = change_direction(init_node,path[i+1],direction)
                    moves.append(turn)
                    steps = abs(path[i][0]-path[i+1][0])
                else:
                    direction,turn = change_direction(init_node,path[i+1],direction)
                    moves.append(turn)
                    steps = abs(path[i][0]-path[i+1][0])
                init_node = path[i+1]
                final_node = path[i+1]
        
        elif direction == 'left' or direction == 'right':
            if path[i][1] == path[i+1][1]:
                steps += abs(path[i][0]-path[i+1][0])
                final_node = path[i+1]

            else:
                if steps>0:
                    movement = get_movement(steps,init_node,final_node,direction)
                
                    moves.append(movement)
                    direction,turn = change_direction(init_node,path[i+1],direction)
                    moves.append(turn)
                    steps = abs(path[i][1]-path[i+1][1])
                else:
                    direction,turn = change_direction(init_node,path[i+1],direction)
                    moves.append(turn)
                    steps = abs(path[i][1]-path[i+1][1])
                init_node = path[i+1]
                final_node = path[i+1]
    
    moves.append(get_movement(steps,init_node,final_node,direction))
    return moves
        


def determine_algo():
    global init_position_x,init_position_y,edge
    algo = ['','','','']
    if edge == "top":
        algo[0] = 'forward'
        algo[3] = 'down'
        if init_position_x<0:
            algo[1] = 'right'
            algo[2] = 'left'
        else:
            algo[1] = 'left'
            algo[2] = 'right'
        return algo
    elif edge == "bottom":
        algo[0] = 'down'
        algo[3] = 'forward'
        if init_position_x<0:
            algo[1] = 'right'
            algo[2] = 'left'
        else:
            algo[1] = 'left'
            algo[2] = 'right'
        return algo

    elif edge == "left":
        algo[0] = 'left'
        algo[3] = 'right'
        if init_position_y<0:
            algo[1] = 'forward'
            algo[2] = 'down'
        else:
            algo[1] = 'down'
            algo[2] = 'forward'
        return algo

    elif edge == "right":
        algo[0] = 'right'
        algo[3] = 'left'
        if init_position_y<0:
            algo[1] = 'forward'
            algo[2] = 'down'
        else:
            algo[1] = 'down'
            algo[2] = 'forward'
        return algo

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    global min_x,max_x,min_y,max_y
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def update_position(position_x,position_y,new_x,new_y):

    if is_position_allowed(new_x, new_y) and not mazeobs.is_path_blocked(position_x,position_y,new_x,new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def get_coord(path):
    return path[len(path)-1]


def check_path_status(path):
    if path[0]=='dead':
        return False
    return True


def get_path_coord():
    """GET PATH COORDINATES
     =======================
     
     - Determines which path is the shortest
     - Starts with one path, it checks which possible direction it can take,
      if there is more than one possibility, then extra path(s) is(are) created
     - which ever path reaches the edge first is the path we take and the
      while loop is stopped when the shortest path is found
      - each path stores a status which could be alive or dead, when 
      a path is dead it removed from the paths
      - each path stores coordinates in the order that the robot nust move by
      - everytime when a coord is visited it is declared as visited 
      node which means we can never visit it again"""
     
    global init_direction,init_position_x,init_position_y,visited_nodes
    paths = []
    visited_nodes.append((init_position_x,init_position_y))
    algo = determine_algo()
    init_path = ('alive',tuple([(init_position_x,init_position_y)]),init_direction)

    paths.append(init_path)

    if (edge == 'left' and init_position_x == -100 or
        edge == 'right' and init_position_x == 100 or 
        edge == 'top' and init_position_y == 200 or 
        edge == 'bottom' and init_position_y == -200):
        return []   
    
    while True:
       
        ####################REMOVE DEAD PATHS#################
        alive_path_iterator = filter(check_path_status,paths)
        paths = list(alive_path_iterator)        
        ####################REMOVE DEAD PATHS#################
        
        
        len_paths = len(paths)
        for path_idx in range(len_paths):
            
            extra_path = False
            curr_x,curr_y = get_coord(paths[path_idx][1])
            temp_path = paths[path_idx]
            nodes = temp_path[1]
            direction = temp_path[2]
            for i in algo:
                
                if i == 'forward' and update_position(curr_x,curr_y,curr_x,curr_y+7) and (curr_x,curr_y+7) not in visited_nodes:
                        visited_nodes.append((curr_x,curr_y+7))
                        nodes = temp_path[1]
                        direction = temp_path[2]
                        if extra_path==True:
                            nodes = nodes + ((curr_x,curr_y+7),)
                            new_path = ('alive',nodes,direction)
                            paths.append(new_path)
                        else:
                            extra_path = True
                            nodes = nodes + ((curr_x,curr_y+7),)
                            paths[path_idx] = ('alive',nodes,direction)
                
                elif i == 'down' and update_position(curr_x,curr_y,curr_x,curr_y-7) and (curr_x,curr_y-7) not in visited_nodes:
                        visited_nodes.append((curr_x,curr_y-7))
                        nodes = temp_path[1]
                        direction = temp_path[2]
                        if extra_path==True:
                            nodes = nodes + ((curr_x,curr_y-7),)
                            new_path = ('alive',nodes,direction)
                            paths.append(new_path)
                        else:
                            extra_path = True
                            nodes = nodes + ((curr_x,curr_y-7),)
                            paths[path_idx] = ('alive',nodes,direction)
                
                elif i == 'left' and update_position(curr_x,curr_y,curr_x-7,curr_y) and (curr_x-7,curr_y) not in visited_nodes:
                        visited_nodes.append((curr_x-7,curr_y))
                        nodes = temp_path[1]
                        direction = temp_path[2]
                        if extra_path==True:
                            nodes = nodes + ((curr_x-7,curr_y),)
                            new_path = ('alive',nodes,direction)
                            paths.append(new_path)
                        else:
                            extra_path = True
                            nodes = nodes + ((curr_x-7,curr_y),)
                            paths[path_idx] = ('alive',nodes,direction)

                elif i == 'right' and update_position(curr_x,curr_y,curr_x+7,curr_y) and (curr_x+7,curr_y) not in visited_nodes:
                        visited_nodes.append((curr_x+7,curr_y),)
                        nodes = temp_path[1]
                        direction = temp_path[2]
                        if extra_path==True:
                            nodes = nodes + ((curr_x+7,curr_y),)
                            new_path = ('alive',nodes,direction)
                            paths.append(new_path)
                        else:
                            extra_path = True
                            nodes = nodes + ((curr_x+7,curr_y),)
                            paths[path_idx] = ('alive',nodes,direction)
                
                elif extra_path == False:
                    paths[path_idx] = ('dead',)
                
                if ((edge == 'top' and visited_nodes[len(visited_nodes)-1][1] == 200) 
                    or (edge == 'bottom' and visited_nodes[len(visited_nodes)-1][1] == -200)
                    or (edge == 'right' and visited_nodes[len(visited_nodes)-1][0] == 100)
                    or (edge == 'left' and visited_nodes[len(visited_nodes)-1][0] == -100)):
                        return paths[path_idx]
                
                elif (edge == 'top' and visited_nodes[len(visited_nodes)-1][1] < 200 <= visited_nodes[len(visited_nodes)-1][1]+8 and update_position(curr_x,curr_y,curr_x,200)):
                            nodes = nodes + ((curr_x,200),)
                            paths[path_idx] = ('alive',nodes,direction)
                            return paths[path_idx]
                elif (edge == 'bottom' and visited_nodes[len(visited_nodes)-1][1] > -200 >= visited_nodes[len(visited_nodes)-1][1]-8 and update_position(curr_x,curr_y,curr_x,-200)):
                            nodes = nodes + ((curr_x,-200),)
                            paths[path_idx] = ('alive',nodes,direction)
                            return paths[path_idx]
                elif (edge == 'right' and visited_nodes[len(visited_nodes)-1][0] < 100 <= visited_nodes[len(visited_nodes)-1][0]+8 and update_position(curr_x,curr_y,100,curr_y)):
                            nodes = nodes + ((100,curr_y),)
                            paths[path_idx] = ('alive',nodes,direction)
                            return paths[path_idx]
                    
                elif (edge == 'left' and visited_nodes[len(visited_nodes)-1][0] > -100 >= visited_nodes[len(visited_nodes)-1][0]-8 and update_position(curr_x,curr_y,-100,curr_y)):
                            nodes = nodes + ((-100,curr_y),)
                            paths[path_idx] = ('alive',nodes,direction)
                            return paths[path_idx]
                    

def mazerunner():
    """MAZERUNNER
      ============
      - Main body of the maze algorithm solver
      - returns a list of commands the robot must follow"""
      
    global init_direction
    path_info = get_path_coord()
    if path_info == []:
        return path_info
    moves = get_moves(path_info[1],init_direction)
    return moves


    