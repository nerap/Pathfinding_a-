import cell


def runner_surround(general_maze, current_maze, x, y):
    """Actualize the current maze of the runner after he movement
    Args :
        general_maze : list of list(grid), the main maze of with every case discovered
        current_maze : List of List(integer), with the value associated to each cell.
        x : Int, current coords to analyze
        y : Int, current coords to analyze
    Returns :
        current_maze : List of List(integer), with the value associated to each cell.
    """

    """if x - 1 >= 0 and y - 1 >= 0:
        if general_maze[y - 1][x - 1] != "1":
            current_maze[y - 1][x - 1] = value_of_the_cell(x - 1, y - 1)

    if x - 1 >= 0 and y + 1 < len(general_maze):
        if general_maze[y + 1][x - 1] != "1":
            current_maze[y + 1][x - 1] = value_of_the_cell(x - 1, y + 1)

    if x - 1 >= 0:
        if general_maze[y][x - 1] != "1":
            current_maze[y][x - 1] = value_of_the_cell(x - 1, y)

    if x + 1 < len(general_maze[y]) and y - 1 >= 0:
        if general_maze[y - 1][x + 1] != "1":
            current_maze[y - 1][x + 1] = value_of_the_cell(x + 1, y - 1)

    if x + 1 < len(general_maze[y]) and y + 1 < len(general_maze):
        if general_maze[y + 1][x + 1] != "1":
            current_maze[y + 1][x + 1] = value_of_the_cell(x + 1, y + 1)

    if x + 1 < len(general_maze[y]):
        if general_maze[y][x + 1] != "1":
            current_maze[y][x + 1] = value_of_the_cell(x + 1, y)

    if y - 1 >= 0:
        if general_maze[y - 1][x] != "1":
            current_maze[y - 1][x] = value_of_the_cell(x, y - 1)

    if y + 1 < len(general_maze):
        if general_maze[y + 1][x] != "1":
            current_maze[y + 1][x] = value_of_the_cell(x, y + 1)
"""
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


def maze(maze_map, start, end):
    current_maze = maze_runner_initialization(maze_map)

    coord = start

    coord[0] -= 1

    coord[1] -= 1

    case = cell.Cell(coord, start)

    print(case)

    pass

