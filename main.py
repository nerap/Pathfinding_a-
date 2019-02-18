import json


def initialization_coord(general_maze, char):
    """From the maze return the initial position of the runner
    Args :
        general_maze: The maze to current maze to perfom
        char : Char, will distinct the start point from end point
    Return :
        x : Int, index of the column
        y : Int, index of the row
    """

    for row in general_maze:
        for column in row:
            if column == char:
                return row.index(column), general_maze.index(row)


if __name__ == "__main__":
    with open('./Grid/grid.json') as grid:
        maze = json.load(grid)

    start_x, start_y = initialization_coord(maze, "S")
    end_x, end_y = initialization_coord(maze, "E")

    
    for i in maze:
        print(i)
    pass
