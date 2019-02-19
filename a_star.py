import cell


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


def maze(maze_map, start, end):
    current_maze = maze_runner_initialization(maze_map)
    temp = []
    temp.append(start[0])
    temp.append(start[1])

    current_maze = runner_surround(maze_map, current_maze, temp[0], temp[1], 0, end)

    while temp[0] != end[0] and temp[1] != end[1]:
        temp = move_next_cell(current_maze)
        current_maze[temp[1]][temp[0]].set_discovered(True)
        current_maze = runner_surround(maze_map, current_maze, temp[0], temp[1], 0, end)


    return current_maze

