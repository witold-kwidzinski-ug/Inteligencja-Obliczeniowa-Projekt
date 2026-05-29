import random
from dfs import dfs

colors = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "green",
    5: "blue",
    6: "cyan",
    7: "pink",
    8: "purple",
    9: "brown",
    10: "grey"
}



def maze_generator(width, height, color_amount):
    maze = [[0 for _ in range(width)] for _ in range(height)]

    while True:
        tmp = [j[:] for j in maze]
        used_points = {}
        for i in range(color_amount):
            used_points[i+1] = []
            valid = False
            while not valid:
                start = (random.randint(0, width-1), random.randint(0, height-1))
                end = (random.randint(0, width-1), random.randint(0, height-1))
                if start not in used_points and end not in used_points:
                    maze[start[1]][start[0]] = i + 1
                    maze[end[1]][end[0]] = i + 1
                    used_points[i+1].append(start)
                    used_points[i+1].append(end)
                    valid = True
        print("Points found")
        if dfs(tmp, used_points):
            return tmp


print(maze_generator(5,4,2))