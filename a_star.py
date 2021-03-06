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
    global start

    if x - 1 >= 0 and y - 1 >= 0:
        if general_maze[x - 1][y - 1] != 1:
            if general_maze[x - 1][y] != 1 or general_maze[x][y - 1] != 1:
                if current_maze[x - 1][y - 1] == "?":
                    current_maze[x - 1][y - 1] = cell.Cell([x - 1, y - 1], [x, y], start, end)
                elif current_maze[x - 1][y - 1].get_discovered() == False:
                    current_maze[x - 1][y - 1].calcul_g_cost(start)
                    current_maze[x - 1][y - 1].calcul_h_cost(end)

    if x + 1 < len(general_maze) and y - 1 >= 0:
        if general_maze[x + 1][y - 1] != 1:
            if general_maze[x + 1][y] != 1 or general_maze[x][y - 1] != 1:
                if current_maze[x + 1][y - 1] == "?":
                    current_maze[x + 1][y - 1] = cell.Cell([x + 1, y - 1], [x, y], start, end)
                elif current_maze[x + 1][y - 1].get_discovered() == False:
                    current_maze[x + 1][y - 1].calcul_g_cost(start)
                    current_maze[x + 1][y - 1].calcul_h_cost(end)

    if y - 1 >= 0:
        if general_maze[x][y - 1] != 1:
            if current_maze[x][y - 1] == "?":
                current_maze[x][y - 1] = cell.Cell([x, y - 1], [x, y], start, end)
            elif current_maze[x][y - 1].get_discovered() == False:
                current_maze[x][y - 1].calcul_g_cost(start)
                current_maze[x][y - 1].calcul_h_cost(end)

    if x - 1 >= 0 and y + 1 < len(general_maze[x]):
        if general_maze[x - 1][y + 1] != 1:
            if general_maze[x - 1][y] != 1 or general_maze[x][y + 1] != 1:
                if current_maze[x - 1][y + 1] == "?":
                    current_maze[x - 1][y + 1] = cell.Cell([x - 1, y + 1], [x, y], start, end)
                elif current_maze[x - 1][y + 1].get_discovered() == False:
                    current_maze[x - 1][y + 1].calcul_g_cost(start)
                    current_maze[x - 1][y + 1].calcul_h_cost(end)

    if x + 1 < len(general_maze) and y + 1 < len(general_maze[x]):
        if general_maze[x + 1][y + 1] != 1:
            if general_maze[x + 1][y] != 1 or general_maze[x][y + 1] != 1:
                if current_maze[x + 1][y + 1] == "?":
                    current_maze[x + 1][y + 1] = cell.Cell([x + 1, y + 1], [x, y], start, end)
                elif current_maze[x + 1][y + 1].get_discovered() == False:
                    current_maze[x + 1][y + 1].calcul_g_cost(start)
                    current_maze[x + 1][y + 1].calcul_h_cost(end)

    if y + 1 < len(general_maze[x]):
        if general_maze[x][y + 1] != 1:
            if current_maze[x][y + 1] == "?":
                current_maze[x][y + 1] = cell.Cell([x, y + 1], [x, y], start, end)
            elif current_maze[x][y + 1].get_discovered() == False:
                current_maze[x][y + 1].calcul_g_cost(start)
                current_maze[x][y + 1].calcul_h_cost(end)

    if x - 1 >= 0:
        if general_maze[x - 1][y] != 1:
            if current_maze[x - 1][y] == "?":
                current_maze[x - 1][y] = cell.Cell([x - 1, y], [x, y], start, end)
            elif current_maze[x - 1][y].get_discovered() == False:
                current_maze[x - 1][y].calcul_g_cost(start)
                current_maze[x - 1][y].calcul_h_cost(end)

    if x + 1 < len(general_maze):
        if general_maze[x + 1][y] != 1:
            if current_maze[x + 1][y] == "?":
                current_maze[x + 1][y] = cell.Cell([x + 1, y], [x, y], start, end)
            elif current_maze[x + 1][y].get_discovered() == False:
                current_maze[x + 1][y].calcul_g_cost(start)
                current_maze[x + 1][y].calcul_h_cost(end)
    return current_maze


def display_retour(general_maze, current_maze, start, end):
    
    enfant = current_maze[end[0]][end[1]]
    compteur = 0
    
    while enfant.get_coord()[0] != start[0] or enfant.get_coord()[1] != start[1]:
        
        compteur += 1
        if compteur > 1000:
            break
        
        coords_parent = enfant.get_coord_parent()
        parent = current_maze[coords_parent[0]][coords_parent[1]]
        mon_cadre.create_line(enfant.get_coord()[0]*30+15,enfant.get_coord()[1]*30+15,parent.get_coord()[0]*30+15,parent.get_coord()[1]*30+15,width=3,fill='black')
        enfant = parent
        
    """x = end[0]
    y = end[1]
    compteur = 0
    while x != start[0] or y != start[1]:
        compteur += 1
        if compteur > 1000:
            break
        min_g = 1000000
        case = current_maze[x][y]
        if x - 1 >= 0 and y - 1 >= 0:
            if general_maze[x - 1][y - 1] != 1:
                if general_maze[x - 1][y] != 1 or general_maze[x][y - 1] != 1:
                    if current_maze[x - 1][y - 1] != "?":
                        if current_maze[x - 1][y - 1].get_discovered() == True:
                            g = current_maze[x - 1][y - 1].get_g_cost()
                            if g < min_g:
                                min_g = g
                                case = current_maze[x - 1][y - 1]
                                
        if x + 1 < len(general_maze) and y - 1 >= 0:
            if general_maze[x + 1][y - 1] != 1:
                if general_maze[x + 1][y] != 1 or general_maze[x][y - 1] != 1:
                    if current_maze[x + 1][y - 1] != "?":
                        if current_maze[x + 1][y - 1].get_discovered() == True:
                            g = current_maze[x + 1][y - 1].get_g_cost()
                            if g < min_g:
                                min_g = g
                                case = current_maze[x + 1][y - 1]
                                
        if y - 1 >= 0:
            if general_maze[x][y - 1] != 1:
                if current_maze[x][y - 1] != "?":
                    if current_maze[x][y - 1].get_discovered() == True:
                        g = current_maze[x][y - 1].get_g_cost()
                        if g < min_g:
                            min_g = g
                            case = current_maze[x][y - 1]
                            
    
        if x - 1 >= 0 and y + 1 < len(general_maze[x]):
            if general_maze[x - 1][y + 1] != 1:
                if general_maze[x - 1][y] != 1 or general_maze[x][y + 1] != 1:
                    if current_maze[x - 1][y + 1] != "?":
                        if current_maze[x - 1][y + 1].get_discovered() == True:
                            g = current_maze[x - 1][y + 1].get_g_cost()
                            if g < min_g:
                                min_g = g
                                case = current_maze[x - 1][y + 1]
    
        if x + 1 < len(general_maze) and y + 1 < len(general_maze[x]):
            if general_maze[x + 1][y + 1] != 1:
                if general_maze[x + 1][y] != 1 or general_maze[x][y + 1] != 1:
                    if current_maze[x + 1][y + 1] != "?":
                        if current_maze[x + 1][y + 1].get_discovered() == True:
                            g = current_maze[x + 1][y + 1].get_g_cost()
                            if g < min_g:
                                min_g = g
                                case = current_maze[x + 1][y + 1]
                           
    
        if y + 1 < len(general_maze[x]):
            if general_maze[x][y + 1] != 1:
                if current_maze[x][y + 1] != "?":
                    if current_maze[x][y + 1].get_discovered() == True:
                        g = current_maze[x][y + 1].get_g_cost()
                        if g < min_g:
                            min_g = g
                            case = current_maze[x][y + 1]
                          
    
        if x - 1 >= 0:
            if general_maze[x - 1][y] != 1:
                if current_maze[x - 1][y] != "?":
                    if current_maze[x - 1][y].get_discovered() == True:
                        g = current_maze[x - 1][y].get_g_cost()
                        if g < min_g:
                            min_g = g
                            case = current_maze[x - 1][y]
                            
    
        if x + 1 < len(general_maze[x]):
            if general_maze[x + 1][y] != 1:
                if current_maze[x + 1][y] != "?":
                    if current_maze[x + 1][y].get_discovered() == True:
                        g = current_maze[x + 1][y].get_g_cost()
                        if g < min_g:
                            min_g = g
                            case = current_maze[x + 1][y]
                            
                            
        mon_cadre.create_line(x*30+15,y*30+15,case.get_coord()[0]*30+15,case.get_coord()[1]*30+15,width=3,fill='black')
        x = case.get_coord()[0]
        y = case.get_coord()[1]"""

def maze_runner_initialization(general_maze):
    """Initialize the maze as the runner point of view
    Args:
        general_maze: List of list(char), the maze to perform
    Returns :
        runner_maze : List of List(integer), with the value associated to each cell.
        Only the cell in range of 1 will be discovered and the end point
    """
    run_maze = []

    for index_column in range(0, len(general_maze)):
        temp = []
        for index_row in range(0, len(general_maze[index_column])):
            temp.append("?")
        run_maze.append(temp)
    return run_maze


def move_next_cell(curr_maze):

    result = 120020
    coord = []
    h_cost = 12301203

    for index_x in range(len(curr_maze)):
        for index_y in range(len(curr_maze[0])):
            temp = curr_maze[index_x][index_y]
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

def display_map(current_maze, start, end):
    for x_case in range(44):
        for y_case in range(27):
            case = current_maze[x_case][y_case]
            if x_case == end[0] and y_case == end[1]:
                color_case(x_case, y_case, "yellow", "", "", "")
            if case != "?":
                if x_case == start[0] and y_case == start[1]:
                    color_case(x_case, y_case, "green", case.get_g_cost(), case.get_h_cost(), case.get_f_cost())
                elif x_case == end[0] and y_case == end[1]:
                    color_case(x_case, y_case, "yellow", case.get_g_cost(), case.get_h_cost(), case.get_f_cost())
                elif case.get_discovered() == True and case.get_printed != True:
                    color_case(x_case, y_case, "red", case.get_g_cost(), case.get_h_cost(), case.get_f_cost())
                    case.set_printed(True)
                elif case.get_discovered() == False:
                    color_case(x_case, y_case, "blue", case.get_g_cost(), case.get_h_cost(), case.get_f_cost())

def display_mur(maze_map):
    for x_case in range(44):
        for y_case in range(27):
            case = maze_map[x_case][y_case]
            if case == 1:
                color_case(x_case, y_case, "gray", "", "", "")
    
def update():
    global current_maze, temp, end, start, maze_map
    if temp[0] != end[0] or temp[1] != end[1]:
        for loop in range(10):
            if temp[0] != end[0] or temp[1] != end[1]:
                temp = move_next_cell(current_maze)
                current_maze[temp[0]][temp[1]].set_discovered(True)
                parent_g_cost = current_maze[temp[0]][temp[1]].get_g_cost()
                current_maze = runner_surround(maze_map, current_maze, temp[0], temp[1], parent_g_cost, end)
            else:
                display_map(current_maze, start, end)
                display_retour(maze_map, current_maze, start, end)
                return current_maze
        
        display_map(current_maze, start, end)
        fen1.after(1, update)
    else:
        display_map(current_maze, start, end)
        display_retour(maze_map, current_maze, start, end)
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

    current_maze[temp[0]][temp[1]] = cell.Cell([temp[0], temp[1]], [temp[0], temp[1]], start, end)
    current_maze[temp[0]][temp[1]].set_discovered(True)
    current_maze[temp[0]][temp[1]].set_g_cost(0)
    current_maze = runner_surround(maze_map, current_maze, temp[0], temp[1], start, end)
    
    
    fen1.resizable(width=False, height=False)
    imageFixe=PhotoImage(file='grilleMap.gif')
    mon_cadre.create_image(0,0,image=imageFixe, anchor=NW)
    display_mur(maze_map)
    mon_cadre.pack()
    update()

    fen1.mainloop()
    #return current_maze
    return None

fen1 = Tk()
mon_cadre = Canvas(fen1,bg='white',height=810,width=1320)
