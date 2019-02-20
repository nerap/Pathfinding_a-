import json
import random
import getCoords
import a_star
import cell


def initialization_coord(general_maze, char):
    """From the maze return the initial position of the runner
    Args :
        general_maze: The maze to current maze to perfom
        char : Char, will distinct the start point from end point
    Return :
        A list with x and y as int
    """
    for index_x in range(len(general_maze)):
        for index_y in range(len(general_maze[0])):
            if general_maze[index_x][index_y] == char:
                return [int(index_x), int(index_y)]


def maze_launch(current_maze, start, end):
    """Will launch one or multiple algorithms to resolve the maze
    Args :
        current_maze: List of list, char, the current maze to perform
        start: List, a vector with the initial start position
        end : List, a vector with the end position
    Returns :
        maze_pathed : The maze with the path to the end
    """

    pass


if __name__ == "__main__":

    maze = getCoords.read_json("./Grid/grid.json")

    maze[22][13] = "S"
    maze[0][0] = "E"

    start_coords = initialization_coord(maze, "S")
    end_coords = initialization_coord(maze, "E")

    print(start_coords)
    print(end_coords)
    
    result = a_star.maze(maze, start_coords, end_coords)

    pass
