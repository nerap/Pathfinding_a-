import cell
from tkinter import *
import random

def runner_surround(general_maze, current_maze, x, y, parent_cell_g_cost, end):
    """Actualize the current maze of the runner after he moves
    Args :
        general_maze : list of list(grid), the main maze of with every case discovered
        current_maze : List of List(integer), with the value associated to each cell.
        x : Int, current coords to analyze
        y : Int, current coords to analyze
    Returns :
        current_maze : List of List(integer), with the value associated to each cell.
    """
    

    if x - 1 >= 0 and y - 1 >= 0:
        if general_maze[y - 1][x - 1] != "1":
            current_maze[y - 1][x - 1] = cell.Cell([x - 1, y - 1], [x, y], parent_cell_g_cost, end)

    if x - 1 >= 0 and y + 1 < len(general_maze):
        if general_maze[y + 1][x - 1] != "1":
            current_maze[y + 1][x - 1] = cell.Cell([x - 1, y + 1], [x, y], parent_cell_g_cost, end)

    if x - 1 >= 0:
        if general_maze[y][x - 1] != "1":
            current_maze[y][x - 1] = cell.Cell([x - 1, y], [x, y], parent_cell_g_cost, end)

    if x + 1 < len(general_maze[y]) and y - 1 >= 0:
        if general_maze[y - 1][x + 1] != "1":
            current_maze[y - 1][x + 1] = cell.Cell([x + 1, y - 1], [x, y], parent_cell_g_cost, end)

    if x + 1 < len(general_maze[y]) and y + 1 < len(general_maze):
        if general_maze[y + 1][x + 1] != "1":
            current_maze[y + 1][x + 1] = cell.Cell([x + 1, y + 1], [x, y], parent_cell_g_cost, end)

    if x + 1 < len(general_maze[y]):
        if general_maze[y][x + 1] != "1":
            current_maze[y][x + 1] = cell.Cell([x + 1, y - 1], [x, y], parent_cell_g_cost, end)

    if y - 1 >= 0:
        if general_maze[y - 1][x] != "1":
            current_maze[y - 1][x] = cell.Cell([x, y - 1], [x, y], parent_cell_g_cost, end)

    if y + 1 < len(general_maze):
        if general_maze[y + 1][x] != "1":
            current_maze[y + 1][x] = cell.Cell([x, y + 1], [x, y], parent_cell_g_cost, end)

    return current_maze


def maze_runner_initialization(general_maze):
    """Initialize the maze as the runner point of view
    Args:
        general_maze: List of list(char), the maze to perform
    Returns :
        runner_maze : List of List(integer), with the value associated to each cell.
        Only the cell in range of 1 will be discovered and the end point
    """
    run_maze = []

    for index_row in range(0, len(general_maze)):
        temp = []
        for index_column in range(0, len(general_maze[index_row])):
            temp.append("?")
        run_maze.append(temp)
    return run_maze


def move_next_cell(curr_maze):

    result = 120020
    coord = []
    h_cost = 12301203

    for index_y in range(len(curr_maze)):
        for index_x in range(len(curr_maze[0])):
            temp = curr_maze[index_y][index_x]
            if temp != "?" and temp.get_discovered() != True:
                if temp.get_f_cost() < result:
                    coord = [index_x, index_y]
                    h_cost = temp.get_h_cost()
                    result = temp.get_f_cost()
                elif temp.get_f_cost == result and temp.get_h_cost() < h_cost:
                    coord = [index_x, index_y]
                    h_cost = temp.get_h_cost()
                    result = temp.get_f_cost()
    return coord




def color_case(x, y, color, g, h, f):
    mon_cadre.create_rectangle(x*30+1,y*30+1,(x+1)*30-1,(y+1)*30-1,fill=color,width=1)
    mon_cadre.create_text(x*30+15, y*30+10, text=str(f), font="Arial 12", fill="black")
    mon_cadre.create_text(x*30+15, y*30+22, text=str(g) + " " + str(h), font="Arial 8", fill="black")

def display_map(current_maze):
    for x_case in range(44):
        for y_case in range(27):
            case = current_maze[x_case][y_case]
            if case != "?":
                color = "blue"
                if case.get_discovered() == True:
                    color = "red"
                color_case(x_case, y_case, color, case.get_g_cost(), case.get_h_cost(), case.get_f_cost())
    
def update():
    global current_maze, temp, end, start, maze_map
    if temp[0] != end[0] and temp[1] != end[1]:
        temp = move_next_cell(current_maze)
        current_maze[temp[1]][temp[0]].set_discovered(True)
        current_maze = runner_surround(maze_map, current_maze, temp[0], temp[1], 0, end)
        
        display_map(current_maze)
        #color_case(random.randrange(0, 44), random.randrange(0, 27), "red", 99, 46, 145)
        fen1.after(1, update)
    else:
        return current_maze

def maze(maze_map1, start1, end1):
    global current_maze, temp, end, start, maze_map
    maze_map = maze_map1
    start = start1
    end = end1
    
    current_maze = maze_runner_initialization(maze_map)
    temp = []
    temp.append(start[0])
    temp.append(start[1])


    current_maze = runner_surround(maze_map, current_maze, temp[0], temp[1], 10, end)
    
    
    fen1.resizable(width=False, height=False)
    imageFixe=PhotoImage(file='grilleMap.gif')
    mon_cadre.create_image(0,0,image=imageFixe, anchor=NW)
    mon_cadre.pack()

    update()

    fen1.mainloop()
    #return current_maze
    return None

fen1 = Tk()
mon_cadre = Canvas(fen1,bg='white',height=810,width=1320)
