import random
from copy import deepcopy
from product import aisles,products
from itertools import permutations

"""Module contains all functionality for the collection of goods step."""

#Using lists as vectors to track position. [0] = Y axis, [1] = X axis.

start_pos = [0,0]
start_char = "S" #character used for visual representation on grid
robot_char = "r" #character used for visual representation on grid

#Grid used for visualizing store layout:
static_grid = [["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],\
              ["-","-","-","-","-","-","-","-"],]

def robot_runtime():
    """Called to start the collection of goods phase."""
    global robot_pos
    randomize_aisle_positions()
    make_grid()
    aisles = get_list_of_aisles_to_visit()
    aisle_positions = []
    for aisle in aisles:
        aisle_positions.append(aisle.position)
    steps, best_path = get_shortest_path(aisle_positions)
    move_robot_along_path(best_path)
    print("Shortest Route = ", str(steps) + " steps.")
    print("Products dispensed. Have a nice rest of your evening!")
    input("Press Enter to exit.")
    exit()

def request_input_to_continue():
    input("Press Enter to continue.")

def randomize_grid_coordinate():
    """Returns randomized vector position."""
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    return [x,y]

def check_unique_coord(a,b):
    return a != b

def randomize_aisle_positions():
    """Ensures each aisle is in its own unique randomized position."""
    for aisle in aisles:
        other_aisles = aisles.copy()
        other_aisles.remove(aisle)
        while True:
            aisle.position = randomize_grid_coordinate()
            unique = True
            if aisle.position == start_pos: #to not overlap with start position
                unique = False
            for other_aisle in other_aisles:
                if not check_unique_coord(aisle.position, other_aisle.position):
                    unique = False
                    break
            if unique:
                break

def make_grid(): 
    """Creates grid with randomized layout."""
    global static_grid
    for aisle in aisles:
        static_grid[aisle.position[0]][aisle.position[1]] = aisle.char
    static_grid[start_pos[0]][start_pos[1]] = "S"
                
def print_grid(grid):
    """Prints grid in readable manner to CLI."""
    grid_str = ''
    for i in range (len(grid)):
        grid_str+="|".join(grid[i])+'\n'
    print(grid_str)

def get_distance_to_pos(from_pos, to_pos):
    """Gets total travel time between two positions."""
    distance_y = abs(from_pos[0] - to_pos[0])
    distance_x = abs(from_pos[1] - to_pos[1])
    return distance_y + distance_x

def get_list_of_aisles_to_visit():
    """Returns list of aisles which contain products requested from user."""
    aisles = []
    for product in products:
        if product.quantity > 0:
            aisles.append(product.aisle)  
    return aisles
            
def get_shortest_path(node_positions):
    """Returns shortest distance and path, visiting each necessary aisle and returning to start."""
    perms = list(permutations(node_positions, len(node_positions)))
    shortest_distance = 9999
    best_perm = []
    for perm in perms:
        distance = 0
        for i in range(0, len(perm)):
            if perm[i] == perm[-1]:
                distance += get_distance_to_pos(perm[0], start_pos)
                distance += get_distance_to_pos(perm[-1], start_pos)
                break
            distance += get_distance_to_pos(perm[i], perm[i+1])
        if distance < shortest_distance:
            shortest_distance = distance
            best_perm = perm
    return shortest_distance, list(best_perm)   

def update_current_grid(new_pos):
    """Updates grid with robot visual position."""
    current_grid = deepcopy(static_grid)
    current_grid[new_pos[0]][new_pos[1]] = robot_char
    return current_grid

def move_robot_along_path(path):
    """Moves robot along the predetermined best path."""
    path.append(start_pos)
    robot_pos = start_pos.copy()
    current_grid = update_current_grid(robot_pos)
    print_grid(current_grid)
    request_input_to_continue()
    for coord in path:
        if coord[0] == robot_pos[0]:
            y_direction = 1
        else:
            y_direction = int((coord[0] - robot_pos[0]) / abs(coord[0] - robot_pos[0]))
        if coord[1] == robot_pos[1]:
            x_direction = 1
        else:
            x_direction = int((coord[1] - robot_pos[1]) / abs(coord[1] - robot_pos[1]))
        while True:
            if robot_pos[0] == coord[0]:
                if robot_pos == coord:
                    break
                else:
                    robot_pos[1] += x_direction
            else:
                robot_pos[0] += y_direction
            current_grid = update_current_grid(robot_pos)
            print_grid(current_grid)
            request_input_to_continue()
                
    