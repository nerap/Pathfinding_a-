import json
import random
import getCoords


def initialization_coord(general_maze, char):
    """From the maze return the initial position of the runner
    Args :
        general_maze: The maze to current maze to perfom
        char : Char, will distinct the start point from end point
    Return :
        A list with x and y as int
    """
    for row in general_maze:
        for column in row:
            if column == char:
                return [row.index(column), general_maze.index(row)]


def maze_launch(current_maze, start, end):
    """Will launch one or multiple algorithms to resolve the maze
    Args :
        current_maze: List of list, char, the current maze to perform
        start: List, a vector with the initial start position
        end : List, a vector with the end position
    Returns :
        maze_pathed : The maze with the path to the end
    """
    path_maze = []
    return path_maze


if __name__ == "__main__":

    maze = getCoords.read_json("./Grid/grid.json")

    maze[random.randint(0, len(maze) - 1)][random.randint(0, len(maze[0]) - 1)] = "S"
    maze[random.randint(0, len(maze) - 1)][random.randint(0, len(maze[0]) - 1)] = "E"

    start_coords = initialization_coord(maze, "S")
    end_coords = initialization_coord(maze, "E")

    for line in maze_launch(maze, start_coords, end_coords):
        print(line)

    for i in maze:
        print(i)

    print(start_coords)
    print(end_coords)
    pass
